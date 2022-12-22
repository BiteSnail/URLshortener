from pydantic import BaseModel
from src.setconfig import get_config
import configparser
class URLItem(BaseModel):
    _id: int
    origin_url: str
    shorten_url: str

class ORIGNITEM(BaseModel):
    origin_url: str

class hash:
    def __init__(self, config:configparser.ConfigParser):
        self.MAP = config['map']
        self.MAXIMUM_ID = int(config['max-id'])
        self.PADDING_WIDTH = int(config['padding-width'])
        self.SPLIT_SEP = int(config['split-sep'])
        self.BASE_NUM = int(config['base-num'])

    def preprocessing(self, origin_url:str)-> bytes:
        origin_url_bytes = origin_url.encode('ascii')
        if len(origin_url_bytes) < self.PADDING_WIDTH:
            origin_url_bytes = origin_url_bytes.zfill(self.PADDING_WIDTH)
        
        return sum([int.from_bytes(origin_url_bytes[i:i+self.SPLIT_SEP], byteorder='big') \
                for i in range(0, len(origin_url_bytes), self.SPLIT_SEP)]) \
                % self.MAXIMUM_ID

    def make_hashable_url(self, origin_url:str) -> str:
        shortURL = ""

        id = self.preprocessing(origin_url)
        # for each digit find the base 62
        while(id > 0):
            shortURL += self.MAP[id % self.BASE_NUM]
            id //= self.BASE_NUM
    
        # reversing the shortURL
        return shortURL[len(shortURL): : -1]

Hash_url = hash(get_config('hash'))