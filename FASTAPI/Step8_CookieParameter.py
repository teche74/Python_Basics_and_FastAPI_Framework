from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, Annotated, Literal

app = FastAPI()

class UserCookie(BaseModel):
    session_id : str = Field(default = None, description="Session ID for the user")
    session_type: Annotated[Literal["admin", "user"], Field(description="Type of session, either 'admin' or 'user'")]
    uptime: Optional[int] = Field(default=None, description="Uptime in seconds")
    session_time : Optional[int] = Field(default=None, description="Session time in seconds")


@app.get('/cookie', response_model=UserCookie)
def get_cookie(session_id: str, session_type: Literal["admin", "user"], uptime: Optional[int] = None, session_time: Optional[int] = None):
    if not session_id:
        raise HTTPException(status_code=400, detail="Session ID is required")
    
    return UserCookie(
        session_id=session_id,
        session_type=session_type,
        uptime=uptime,
        session_time=session_time
    )