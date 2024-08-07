from fastapi import FastAPI
from enum import Enum


app = FastAPI()


@app.get("/")
# async def root():
def root():
    return {"message": "Hello World!!"}


@app.get("/home")
def home():
    return {"message": "home"}


@app.get("/home/{name}")
def read_name(name: str):
    return {"name": name}


@app.get("/home_err/{name}")
def read_name_err(name: int):
    return {"name": name}


def get_name_with_age(name: str, age: int):
    name_with_age: str = name + " is this old: " + age
    return name_with_age


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resent"
    lenet = "lenet"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name is ModelName.lenet:
        return {"model_name": model_name, "message": "LwXNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

    ################################################


@app.get("/items/{item_id}")
def read_item(item_id: str, skip: int = 0, limit: int = 10):
    fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
    print(item_id, skip, limit)
    print(fake_items_db[0:3])
    return fake_items_db[skip : skip + limit]

# @app.post("/")
# def home_post(msg: str):
#     return {"Hello": "POST", "msg": msg}

from pydantic import BaseModel

class DataInput(BaseModel):
    name: str

@app.post("/")
def home_post(data_request: DataInput):
    return {"Hello": "POST", "msg": data_request.name}