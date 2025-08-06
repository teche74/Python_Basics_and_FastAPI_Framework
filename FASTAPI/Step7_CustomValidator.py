from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel,Field, AfterValidator
from typing import Annotated, Optional, Literal

app = FastAPI()

class User(BaseModel):
    user_name : str | None = Field(default = None, min_length=5 , max_length=50, description = "User First Name and Last Name")
    user_id : int | None = Field(default = None, ge=1, description = "User ID must be greater than 0")
    user_phone : str | None = Field(default = None, min_length=10, max_length=15, description = "User Phone Number must be 10 to 15 digits")
    user_email : str | None = Field(default = None, pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$', description = "User Email must be a valid email format")
    user_status : Literal['active', 'inactive'] = 'active'
    user_job_profile : Literal['engineer', 'manager', 'hr', 'teamlead'] = 'engineer'
    user_address : str | None = Field(default = None, min_length=5, max_length=100, description = "User Address must be at least 5 characters long")    


def ValidUser(user_data : User):
    if user_data.user_name is None or len(user_data.user_name) < 3:
        return False
    if user_data.user_id is None or user_data.user_id <= 0:
        return False
    if user_data.user_phone is None or len(user_data.user_phone) < 10:
        return False
    if user_data.user_email is None or "@" not in user_data.user_email:
        return False
    if user_data.user_address is None or len(user_data.user_address) < 5:
        return False
    return True

@app.post('/validate_string/{input}')
def validate(input : Annotated[ User , Query(description = "User details for validation")]):
    if not ValidUser(input):
        raise HTTPException(status_code=400, detail="Invalid user data")
    return {"message": "User data is valid", "user": input}
        
    