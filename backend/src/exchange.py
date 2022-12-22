from src.database import find_in_db, insert_item_to_db
from src.itemclass import make_hashable_url, ORIGNITEM

site_domain = "http://localhost:3000/"

def exchange_url(originItem:ORIGNITEM):
    #TODO : find originItem in DB
    item = find_in_db(originItem.origin_url)

    if item == None:
        shorten_id = make_hashable_url(originItem.origin_url)
        insert_item_to_db(originItem.origin_url, shorten_id)
    else:
        shorten_id = item['shorten']
    
    return {"shorten_url" : site_domain+shorten_id}