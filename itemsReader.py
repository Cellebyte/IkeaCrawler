import sys
import json


#global variables
item_ids = {}
COUNTRY = 'DE'

def main():
    """main function for parsing"""
    if sys.argv[1] and sys.argv[2]:
        readfile, writefile = open_files(sys.argv[1], sys.argv[2])
        json_items = read_json_file(readfile)
        writefile.write('[\n')
        for json_item in json_items:
            try:
                if item_id_unique(json_item['item_id'][0]) and item_in_de(json_item):
                        write_json_file(writefile, json_item)
                else:
                    print(json_item['item_id'], "already processed")
            except IndexError:
                print("Ignore json_item:\n\t{}".format(json_item))
        print("Looks like I am done!!")
        writefile.seek(0)
        processed = writefile.readlines()
        print( processed[len(processed)-1][:-2])
        processed[len(processed)-1] = processed[len(processed)-1][:-2] + '\n'
        writefile.seek(0)
        writefile.writelines(processed)
        writefile.write(']\n')
        close_files(readfile, writefile)


def open_files(readfilename, writefilename):
    """Function to open the files """
    try:
        readfile = open(readfilename, "r")
        writefile = open(writefilename, "w+")
    except IOError:
        print("Ups, something went wrong with file openings!")
        exit()
    return readfile, writefile


def close_files(readfile, writefile):
    """Function to open the files """
    try:
        readfile.close()
        writefile.close()
    except IOError:
        print("Ups, something went wrong with file closings!")
        exit()
    pass


def write_json_file(filename, json_item):
    """Function for writing an item in a Json file"""
    try:
        # This tries to open an existing file but creates a new file if necessary.
        filename.write(json.dumps(json_item,ensure_ascii=False) + ',\n')
    except IOError:
        print("Ups, something went wrong when writing the file")
        exit()
    pass


def item_id_unique(item_id):
    """Function to check if the item_id has been already dumped"""
    global item_ids
    print("Item id", item_id.encode('utf-8'))
    try:
        if item_ids[item_id.encode('utf-8')]:
            print(item_id, "already exists in the hash table")
            return False
    except KeyError:
        item_ids[item_id.encode('utf-8')] = True
        return True
    pass

def item_in_de(json_item):
    try:
        country = json_item['country']
    except (KeyError,IndexError):
        return False
    if COUNTRY in country:
        return True
    return False


def read_json_file(json_items_file):
    """This function reads the file passed as arg and load the array of jsons"""
    try:
        return json.load(json_items_file)
    except IOError:
        print("Ups, looks like that file does not exists")
        exit()
    pass


def item():
    """docstring for fname"""
    pass
if __name__ == '__main__':
    main()
