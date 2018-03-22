import sys
import couchdb
import json
SERVER = couchdb.client.Server(url="http://admin:admin@127.0.0.1:5984")


def import_db(filename):
    try:
        db = SERVER.create('crawler')
    except (couchdb.http.PreconditionFailed):
        db = SERVER['crawler']
    with open(filename, 'r') as json_data:
        data = json.load(json_data)
    for item in data:
        try:
            doc = db[item['item_id'][0]]
            doc['description'] = item['description']
            doc['keywords'] = item['keywords']
            doc['country'] = item['country']
            doc['language'] = item['language']
            doc['store_id'] = item['store_id']
            doc['title'] = item['title']
            doc['product_name'] = item['product_name']
            doc['category_name'] = item['category_name']
            doc['subcategory_id'] = item['subcategory_id']
            doc['price'] = item['price']
            doc['price_other'] = item['price_other']
            doc['changed_family_price'] = item['changed_family_price']
            doc['changed_family_price_other'] = item['changed_family_price_other']
            doc['item_id'] = item['item_id']
            doc['partnumber'] = item['partnumber']
            doc['url'] = item['url']
            doc['image'] = item['image']
            db.save(doc)
        except couchdb.http.ResourceNotFound:
            db[item['item_id'][0]] = item

if __name__ == "__main__":
    import_db(sys.argv[1])