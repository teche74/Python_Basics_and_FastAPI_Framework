from fastapi import FastAPI , File , UploadFile
from typing import Optional , Annotated
from pydantic import BaseModel, Field


app = FastAPI()


class FileModel(BaseModel):
    file_url : str | None = Field(default = None , description="URL of the uploaded file")
    file_name : str | None = Field(default = None , description="Name of the uploaded file")
    file_size : Optional[int] = Field(default=None, description="Size of the uploaded file  in bytes")


@app.post('/upload_file' , response_model = FileModel)
def upload_file(file : FileModel = File(default = bytes ) , file_name : Optional[str | None] = None):
    if not file:
        raise HTTPException(status_code=400, detail="File is required")
    
    file_url = "http://example.com/files/" + file.file_name if file.file_name else None
    file_size = len(file.file_url) if file.file_url else None
    
    return FileModel(
        file_url=file_url,
        file_name=file.file_name if file_name is not None else "default.txt",
        file_size=file_size
    )