from pydantic import BaseModel
from datetime import datetime, time
from typing import Optional
from uuid import UUID

class seatSchedsCreate(BaseModel):
    scheduleId: UUID
    seatId: UUID
    status: str
    
class seatSchedsUpdate(seatSchedsCreate):
    status: Optional[str] = None

class seatSchedsDelete(BaseModel):
    message: str

class seatSchedBase(seatSchedsCreate):
    id: UUID
    created_at: datetime
    delete_exp: Optional[datetime] = None
    is_delete: bool
    
    class Config:
          from_attributes = True  

class seatsCreate(BaseModel):
      roomId: UUID
      seat_num: str
      types: str
      row: str
      x_position: int
      y_position: int
      rotations: int
      
class seatsUpdate(seatsCreate):
      seat_num: Optional[str] = None
      types: Optional[str] = None
      row: Optional[str] = None

class seatsDelete(BaseModel):
      message: str

class seatsBase(seatsCreate):
      id: UUID
      created_at: datetime
      delete_exp: Optional[datetime] = None
      is_delete: bool   
      
      class Config:
          from_attributes = True   