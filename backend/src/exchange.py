from src.database import db, reverse_db, is_in_db, insert_item_to_db
from src.itemclass import URLItem

site_domain = "http://localhost:3000/"

def exchange_url(originItem):
    #TODO : find originItem in DB

    if is_in_db(originItem.origin_url):
        shorten_url = db[originItem.origin_url]
    else:
        shorten_url = URLItem.make_short_url(originItem.origin_url)
        insert_item_to_db(originItem.origin_url, shorten_url)
    
    return {"shorten_url" : site_domain+shorten_url[:5]}