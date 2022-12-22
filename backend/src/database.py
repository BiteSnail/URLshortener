from pymongo import MongoClient

hostname = 'localhost'
portnum = 27017
databasename = 'test'
collectionname = 'urlitem'

Client = MongoClient(host=hostname, port=portnum)
db = Client[databasename]
items = db[collectionname]

def insert_item_to_db(origin, shorten):
    item = {"origin": origin,
            "shorten": shorten}
    item_id = items.insert_one(item).inserted_id

def find_in_db(origin):
    return items.find_one({"origin":origin})

def link_in_db(shorten_id):
    return items.find_one({"shorten":shorten_id})['origin']