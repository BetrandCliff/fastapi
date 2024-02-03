from fastapi import FastAPI
from  pydantic import BaseModel
from typing import Optional
from . import schemas


app = FastAPI()


@app.get("/")

def index(limit:int, published:bool, sort:  Optional[str]=None):
    if published:

        return f"{limit} is the limit of the current data fetch from the database"
    else:
        return f"{limit} is not published"


@app.post("/blog")

def create(request:schemas.Blog):

    return request.title