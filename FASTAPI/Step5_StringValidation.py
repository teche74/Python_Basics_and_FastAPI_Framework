from fastapi import FastAPI, Query
from typing import Annotated, Optional
from pydantic import BaseModel

app= FastAPI()

class Item(BaseModel):
    price : int
    description : str | None 
    tax : int
    product_id : int
    expiry_months : int
    
@app.post("/medic/{medicine_name}_{desc}")
def GetMedicineInfo(medicine_name :str, info : Item , tax : Optional[int] = Query(default=None) , desc : str = "No Description Available" , exp : Optional[int] = Query(default=12)):
    result = info.model_dump()
    result["product_id"] = 12
    result["price"] = 10
    result["tax"] = result["price"] + (tax if tax is not None else 10)
    result["description"] = desc
    result["expiry_months"] = exp
    
    return {
        "medicine_name" : medicine_name.title(),
        "data" : result,
        "message" : "infomation available fetched"
    }