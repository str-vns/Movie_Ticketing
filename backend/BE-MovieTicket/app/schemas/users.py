from pydantic import BaseModel,EmailStr
from datetime import datetime

class UserBase(BaseModel):
    firstName: str
    lastName: str
    pfp: str
    email: EmailStr
    lastName: str
class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    firstName: str
    lastName: str
    
class UserCreate(UserBase):
    password: str
    
class LoginUser(BaseModel):
    password:str
    
class User(UserBase):
    id: str
    is_active: bool
    created_at: datetime
    
    class Config:
        from_attributes = True
    