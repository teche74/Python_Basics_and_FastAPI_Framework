from fastapi import FastAPI, Form , HTTPException
from pydantic import BaseModel, Field
from typing import Optional, Annotated, Literal , EmailStr


app = FastAPI()

class UserFormData(BaseModel):
    user_name : str | None = Field(default = None , min_length = 5 , max_lenght = 10 , description = "Name of the user")
    user_email : EmailStr | None = Field(default = None , description = "Email of the user")
    user_age : Optional[int] = Field(default=None, description="Age of the user")
    user_type: Annotated[Literal["admin", "user"], Field(description="Type of user, either 'admin' or 'user'")]


@app.post('/formdata', response_model=UserFormData)
def post_form_data( user_name : Annotated[str , Form()], user_email : Annotated[EmailStr , Form()], user_age : Optional[int] = Form(default=None), user_type: Annotated[Literal["admin", "user"] , Field(description="Type of user, either 'admin' or 'user'")] = Form(default="user")):
    if not user_name or len(user_name) < 5 or len(user_name) > 10:
        raise HTTPException(status_code=400, detail="User name must be between 5 and 10 characters")
    
    return UserFormData(
        user_name=user_name,
        user_email=user_email,
        user_age=user_age,
        user_type=user_type
    ) 