from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.setconfig import check_config
check_config()
from src.linktosite import link_to_site
from src.exchange import exchange_url
from src.itemclass import ORIGNITEM
import uvicorn

app = FastAPI()

origins = {
    "http://localhost",
    "http://localhost:3000",
}

app.add_middleware(
   CORSMiddleware,
    allow_origins = origins,
    allow_credentials =True,
    allow_methods = ["*"],
    allow_headers= ["*"],
)

@app.get('/{hashed_id}')
async def link(hashed_id: str):
    return link_to_site(hashed_id)

@app.post('/api/exchange')
async def exchange(originItem:ORIGNITEM):
    return exchange_url(originItem)

@app.post('/api/verify')
async def verify(originItem:ORIGNITEM):
    whitelist = ('http://', 'https://')
    result = originItem.origin_url.startswith(whitelist)
    print(result)
    return {"result":result}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)