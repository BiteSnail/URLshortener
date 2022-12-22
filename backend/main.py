from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.exchange import exchange_url
from src.database import link_in_db
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
async def link_to_site(hashed_id: str):
    shorten_id = link_in_db(hashed_id)
    if shorten_id == None:
        return {"origin_url" : "error"}
    else:
        return {"origin_url" : shorten_id}

@app.post('/exchange')
async def exchange(originItem:ORIGNITEM):
    return exchange_url(originItem)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)