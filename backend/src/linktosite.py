from fastapi import FastAPI
from src.database import db

def link_to_site(hashed_id: str):
    shorten_id = db.link_in_db(hashed_id)
    if shorten_id == None:
        return {"origin_url" : "error"}
    else:
        return {"origin_url" : shorten_id}