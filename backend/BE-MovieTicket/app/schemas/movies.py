from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from uuid import UUID

class MovieSchedBase(BaseModel):
      start_time : str
      price: float
      
class MovieSchedCreate(MovieSchedBase):
      available_seat: int
      total_seat: int
      movieId: str
      date: str
      
class MoviesSchedUpdate(MovieSchedCreate):
    available_seat: Optional[int] = None
    total_seat: Optional[int] = None
    start_time: Optional[str] = None 
    date: Optional[str] = None
    price: Optional[float] = None
  
  
class MovieScheds(MovieSchedBase):
    id: UUID
    movieId: UUID
    created_at: datetime
    delete_exp: Optional[datetime] = None
    is_delete: bool
    class Config:
        from_attributes = True
        
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
    id: UUID
    created_at: datetime
    delete_exp: Optional[datetime] = None
    is_delete: bool
    class Config:
        from_attributes = True