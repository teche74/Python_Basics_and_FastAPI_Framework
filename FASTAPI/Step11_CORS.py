from fastapi import FastAPI, Query , HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional, Annotated, Literal

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = [
        "http://localhost:3000",
        "https://example.com",
        "..."
    ],
    allow_credentials = True,
    allow_methods  = ["GET" , "POST", "PUT", "DELETE"],
    allow_headers = ["*"]
)


@app.get('/cors', response_model=Annotated[Literal["success", "failure"], Field(description="Response status")])
def get_cors(
    origin: Annotated[str, Query(description="Origin of the request")] = "http://localhost:3000",
    method: Annotated[Literal["GET", "POST", "PUT", "DELETE"], Query(description="HTTP method used")] = "GET"
):
    if origin not in ["http://localhost:3000", "https://example.com"]:
        raise HTTPException(status_code=403, detail="CORS policy does not allow this origin")
    
    return "success"    

