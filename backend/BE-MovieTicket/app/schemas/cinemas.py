from pydantic import BaseModel
from datetime import datetime, time
from typing import Optional
from uuid import UUID

class RoomsCreate(BaseModel):
    roomInfo: str
    cinemaId: UUID
    status: str
    
class RoomsUpdate(RoomsCreate):
     roomInfo: Optional[str] = None
     status: Optional[str] = None
     
class RoomsDelete(BaseModel):
    message: str

class RoomsBase(RoomsCreate):
    id: UUID
    created_at: datetime
    delete_exp: datetime
    is_delete: bool
    class Config:
        from_attributes = True

    
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
    delete_exp: datetime
    is_delete: bool
    class Config:
        from_attributes = True