from pymongo import MongoClient
from src.setconfig import get_config
import configparser

class DataBase:
    def __init__(self, config:configparser.ConfigParser):
        self.Client = MongoClient(host=config['host'], port=int(config['port']))
        self.items = self.Client[config['database']][config['collection']]
    
    def insert_item_to_db(self, origin:str, shorten:str):
        item = {"origin": origin,
                "shorten": shorten}
        item_id = self.items.insert_one(item).inserted_id

    def find_in_db(self, origin:str):
        return self.items.find_one({"origin":origin})

    def link_in_db(self, shorten_id:str):
        return self.items.find_one({"shorten":shorten_id})['origin']

db = DataBase(get_config('mongodb'))