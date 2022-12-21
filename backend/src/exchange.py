from src.database import db, is_in_db, insert_item_to_db
from src.itemclass import make_hashable_url, ORIGNITEM

site_domain = "http://localhost:3000/"

def exchange_url(originItem:ORIGNITEM):
    #TODO : find originItem in DB

    if is_in_db(originItem.origin_url):
        shorten_url = db[originItem.origin_url]
    else:
        shorten_url = make_hashable_url(originItem.origin_url)
        insert_item_to_db(originItem.origin_url, shorten_url)
    
    return {"shorten_url" : site_domain+shorten_url[:5]}