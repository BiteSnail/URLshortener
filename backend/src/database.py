from pymongo import MongoClient
import pymongo
from src.setconfig import get_config
import configparser

class Cache:
    def __init__(self, config:configparser.ConfigParser):
        self._storage = {}
        self.capacity = int(config['capacity'])
        self.size = int(config['size'])
    
    def find_item(self, shorten_id:str) -> dict | None:
        if shorten_id in self._storage:
            return {'origin': self._storage[shorten_id],
                    'shorten': shorten_id}
        else:
            return None
    
    def insert_item(self, item:dict):
        if self.size < self.capacity:
            self._storage.update(item)
        else:
            self._storage.popitem()
            self._storage.update(item)
class DataBase:
    def __init__(self, config:configparser.ConfigParser):
        try:
            self.Client = MongoClient(host=config['host'], 
                                    port=int(config['port']), 
                                    serverSelectionTimeoutMS=int(config['maxSevSelDelay']))
            self.Client.server_info()
        except pymongo.errors.ServerSelectionTimeoutError as err:
            print(err)
            exit()

        self.items = self.Client[config['database']][config['collection']]
        self.cache = Cache(get_config('cache'))
    
    def insert_item_to_db(self, origin:str, shorten:str):
        item = {"origin": origin,
                "shorten": shorten}
        try:
            item_id = self.items.insert_one(item).inserted_id
        except pymongo.errors.ServerSelectionTimeoutError as err:
            print(err)

    def find_in_db(self, key:str, value:str)-> dict | None:
        try:
            return self.items.find_one({key:value})
        except pymongo.errors.ServerSelectionTimeoutError as err:
            print(err)
            return None

    def link_in_db(self, shorten_id:str)-> dict | None:
        try:
            return self.items.find_one({"shorten":shorten_id})['origin']
        except pymongo.errors.ServerSelectionTimeoutError as err:
            print(err)
            return None
    
    def find_in_cache(self, shorten_id: str)-> dict | None:
        if shorten_id in self.cache:
            return {"origin": self.cache[shorten_id],
                    "shorten": shorten_id}
        else:
            return None

db = DataBase(get_config('mongodb'))