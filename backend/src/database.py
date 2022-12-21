db = {}
reverse_db = {}

def insert_item_to_db(origin, shorten):
    db[origin] = shorten
    reverse_db[shorten[:5]] = origin

def is_in_db(origin):
    return origin in db