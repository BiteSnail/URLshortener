from src.database import db
from src.itemclass import Hash_url, ORIGNITEM

site_domain = "http://localhost:3000/"

def exchange_url(originItem:ORIGNITEM):
    shorten_id = Hash_url.make_hashable_url(originItem.origin_url)

    item = db.cache.find_item(shorten_id)
    if not item == None:
        return {"shorten_url" : site_domain+shorten_id}

    db.cache.insert_item({shorten_id:originItem.origin_url})
    item = db.find_in_db(key='shorten', value=shorten_id)
    if item == None:
        db.insert_item_to_db(originItem.origin_url, shorten_id)
    else:
        shorten_id = item['shorten']
    
    return {"shorten_url" : site_domain+shorten_id}