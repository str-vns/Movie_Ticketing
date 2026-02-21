import jwt
import os
from datetime import datetime, timedelta, timezone
from jwt.exceptions import InvalidTokenError
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

class Token(BaseModel):
    access_token: str
    token_type: str
    
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utz) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, os.getenv("SecretKey"), algorithm=os.getenv("ALGO"))
    return encoded_jwt