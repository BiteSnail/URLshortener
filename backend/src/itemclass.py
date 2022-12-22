from pydantic import BaseModel
import base64

class URLItem(BaseModel):
    _id: int
    origin_url: str
    shorten_url: str

class ORIGNITEM(BaseModel):
    origin_url: str

def make_hashable_url(origin_url:str) -> str:
    origin_url_bytes = origin_url.encode('ascii')
    origin_url_base64 = base64.b64encode(origin_url_bytes)
    origin_url_base64_str = origin_url_base64.decode('ascii')
    return origin_url_base64_str
