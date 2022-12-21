from fastapi import FastAPI
from src.exchange import exchange_url
from src.database import db, reverse_db
import uvicorn

app = FastAPI()

@app.get('/{hashed_id}')
async def link_to_site(hashed_id: str):
    for item in reverse_db:
        if item[:5] == hashed_id:
            return {"origin_url" : reverse_db[item]}
    return {"origin_url" : "error"}

@app.post('/exchange')
async def exchange(originItem):
    return exchange_url(originItem)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)