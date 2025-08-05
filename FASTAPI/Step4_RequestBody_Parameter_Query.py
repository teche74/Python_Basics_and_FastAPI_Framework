from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
app = FastAPI()


class Item(BaseModel):
    product_name : str
    product_price : int
    product_description : str | None
    product_id : int


@app.post("/items/{item_id}")
def update(item : Item , item_id : int , tax_percent : Optional[int]):
    result = {
        "tax_price" : item.product_price+ ((tax_percent/100) * item.product_price),
        **item.model_dump()
    }
    return result
    
