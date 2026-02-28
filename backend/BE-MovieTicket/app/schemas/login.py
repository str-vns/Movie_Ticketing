from pydantic import BaseModel,EmailStr
from datetime import datetime
from uuid import UUID

class UserLogin(BaseModel):
      email: EmailStr
      password: str


class Token(BaseModel):
    User: dict = {
        "id": str | None,
        "firstName": str | None,
        "lastName": str | None,
        "email": EmailStr,
        "pfp": str | None
    }
    access_token: str
    token_type: str
    accessDay: datetime
    expireDay: datetime

class TokenData(BaseModel):
    email: EmailStr | None = None