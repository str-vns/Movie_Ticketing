from pydantic import BaseModel
from datetime import datetime

class MoviesCreate(BaseModel):
      title: str
      synopsis: str
      image: str
      duration: str
      release: str

class MoviesOut(MoviesCreate):
    id: str
    created_at: datetime
    is_delete: bool
    class Config:
        from_attributes = True