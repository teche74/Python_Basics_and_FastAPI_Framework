from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()


class Item(BaseModel):
    product_name : str
    product_price : int
    product_description : str | None = None
    product_id : int


@app.put("/items/")
def update(item : Item):

    return {
        "data" : item,
        "message": "Item updated successfully"
    }
