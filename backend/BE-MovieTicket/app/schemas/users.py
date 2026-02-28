from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional
class UserBase(BaseModel):
    firstName: str
    lastName: str
    pfp: str
    email: EmailStr
class UserCreate(UserBase):
    password: str
class UserUpdate(UserBase):
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    pfp: Optional[str] = None
    email: Optional[str] = None 
    is_active: Optional[bool] = None
class User(UserBase):
    id: str
    is_active: bool
    created_at: datetime
    
    class Config:
        from_attributes = True
    