from pydantic import BaseModel
from datetime import datetime, time
from typing import Optional

class CinemasCreate(BaseModel):
      cinemaName: str
      cinemaAddress: str
      cinemaOpen: time
      cinemaClose: time
      cinemaSched: str
      
class CinemasUpdate(CinemasCreate):
    cinemaName: Optional[str] = None
    cinemaAddress: Optional[str] = None
    cinemaOpen: Optional[time] = None
    cinemaClose: Optional[time] = None 
    cinemaSched: Optional[str] = None

class CinemasDelete(BaseModel):
    message: str
    
class CinemasOut(CinemasCreate):
    id: str
    created_at: datetime
    is_delete: bool
    class Config:
        from_attributes = True