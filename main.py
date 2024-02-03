from typing import Union

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}



@app.get('/blog_param')
def blog_param(limit,published:bool, sort:Optional[str]=""):

    if published:

        return {"data":f'{limit} blog from our database'}
    else:
        return {"data":"the data has not been published"}

        

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get('/blog/{id}')
def blog(id:int):

    return {"data":{id:{"this isthe blog and idex "}}}


class Users(BaseModel):
    name:str
    tel:int
    address:str


@app.post('/users')
def user(user:Users):

    return {"data":{ "your name is {user.name} and your telephone is {user.tel} and address is {user.address}"}}
