from pydantic import BaseModel

MAP = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
MAXIMUM_ID = 916132831
PADDING_WIDTH = 2048
SPLIT_SEP = 4
BASE_NUM = len(MAP)
class URLItem(BaseModel):
    _id: int
    origin_url: str
    shorten_url: str

class ORIGNITEM(BaseModel):
    origin_url: str

def preprocessing(origin_url:str)-> bytes:
    origin_url_bytes = origin_url.encode('ascii')
    if len(origin_url_bytes) < PADDING_WIDTH:
        origin_url_bytes = origin_url_bytes.zfill(PADDING_WIDTH)
    
    return sum([int.from_bytes(origin_url_bytes[i:i+SPLIT_SEP], byteorder='big') \
            for i in range(0, len(origin_url_bytes), SPLIT_SEP)]) \
            % MAXIMUM_ID

def make_hashable_url(origin_url:str) -> str:
    shortURL = ""

    id = preprocessing(origin_url)
    # for each digit find the base 62
    while(id > 0):
        shortURL += MAP[id % BASE_NUM]
        id //= BASE_NUM
  
    # reversing the shortURL
    return shortURL[len(shortURL): : -1]
