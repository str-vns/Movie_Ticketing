from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional, List

class PaymentBase(BaseModel):
    accountNum: str
    
class PaymentCreate(PaymentBase):
    accountName: Optional[str] = None 
    cvc: Optional[str] = None 
    exp: Optional[str] = None 
    cardType: str
    cardBranch: str
    userId: str

class PaymentOp(PaymentBase):
    id: str
    userId: str
    created_at: datetime
    class Config:
        from_attributes = True
        
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
    
class LoginUser(BaseModel):
    email: EmailStr
    password: str
    
class User(UserBase):
    id: str
    is_active: bool
    created_at: datetime
    delete_exp: Optional[datetime] = None
    paymentOption: List[PaymentOp] = []
    class Config:
        from_attributes = True


    