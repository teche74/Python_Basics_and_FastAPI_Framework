from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    product_name: str
    product_price: int
    product_description: str | None = None
    product_id: int

@app.put("/items/{item_id}")
def update(item : Item , item_id : int):
    updated_item = item.model_copy(update={
        "product_name": "Mouth Gel",
        "product_id": item_id,
        "product_price": 100,
        "product_description": "This is a mouth gel"
    })

    return {
        "data" : updated_item,
        "message": "Item updated successfully"
    }