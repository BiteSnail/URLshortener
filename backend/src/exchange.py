from src.database import db
from src.itemclass import Hash_url, ORIGNITEM

site_domain = "http://localhost:3000/"

def exchange_url(originItem:ORIGNITEM):
    item = db.find_in_db(originItem.origin_url)
    print(item)

    if item == None:
        shorten_id = Hash_url.make_hashable_url(originItem.origin_url)
        db.insert_item_to_db(originItem.origin_url, shorten_id)
    else:
        shorten_id = item['shorten']
    
    return {"shorten_url" : site_domain+shorten_id}