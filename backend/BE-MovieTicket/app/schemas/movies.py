from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class MoviesCreate(BaseModel):
      title: str
      synopsis: str
      image: str
      duration: str
      release: str
      
class MoviesUpdate(MoviesCreate):
    title: Optional[str] = None
    synopsis: Optional[str] = None
    image: Optional[str] = None
    duration: Optional[str] = None 
    release: Optional[str] = None

class MoviesDelete(BaseModel):
    message: str
    
class MoviesOut(MoviesCreate):
    id: str
    created_at: datetime
    is_delete: bool
    class Config:
        from_attributes = True