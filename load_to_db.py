import sys
import couchdb
import json
import copy
SERVER = couchdb.client.Server(url="http://admin:admin@127.0.0.1:5984")

ITEM_IDS = {}

regexes = {
    'sofas': [
        r'^.*?"keywords": \[".*sofa.*$'
    ],
    'betten': [
        r'^.*bettgestell.*$',
        r'^.*bettrahmen.*$',
        r'^.*tagesbett.*$'
    ],
    'kallax': [
        r'^.*kallax.*$',
        r'^.*dröna.*$'
    ],
    'Schränke': r'' 
}

def handle_store(db,data):
    try:
        new = True
        db = SERVER.create(db)
    except (couchdb.http.PreconditionFailed):
        new = False
        db = SERVER[db]
    for item in data:
        if new:
            try:
                db[item['item_id'][0]] = item
            except IndexError:
                print("no_item_id:\n{}\nIgnoring it".format(item))
                pass
        else:
            try:
                doc = db[item['item_id'][0]]
                for key in item.keys():
                    if not 'item_id' in key:
                        doc[key] = item[key]
                db.save(doc)
            except couchdb.http.ResourceNotFound:
                try:
                    db[item['item_id'][0]] = item
                except IndexError:
                    print("no_item_id:\n{}".format(item))
                    pass
            except IndexError:
                print("no_item_id:\n{}\nIgnoring it".format(item))

def merge(key, value):
    """Function to check if the item_id has been already dumped"""
    global ITEM_IDS
    print("Key", key)
    try:
        ITEM_IDS[key].append(copy.deepcopy(value))
    except (KeyError,AttributeError):
        ITEM_IDS[key] = [ copy.deepcopy(value) ]
        pass
    pass

def flatten(list_of_lists):
    '''
    Makes a list of lists flatten
    @param  l          list
    @return l          flattened list
    [[1,2,3][4,5,6]]
    gets
    [1,2,3,4,5,6]
    '''
    return [item for sublist in list_of_lists for item in sublist]

if __name__ == "__main__":
    with open(sys.argv[1], 'r') as import_file:
        json_items = json.load(import_file)
    
    for json_item in json_items:
        merge(json_item['subcategory_id'][0],json_item)
    with open('test.json', 'w') as json_pt:
        json_pt.write(json.dumps(ITEM_IDS,ensure_ascii=False))