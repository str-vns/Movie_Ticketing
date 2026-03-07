import jwt
import app.schemas.login as schema_login
import app.models.users as models
from datetime import datetime, timedelta, timezone
from jwt.exceptions import InvalidTokenError
from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.dependecy import get_db
from app.core.config import settings
from app.core.security import decrypt_data

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    if not settings.SECRET_KEY:
        raise RuntimeError("SECRET_KEY is not configured")
    encoded_jwt = jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )
    return encoded_jwt

def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
      
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM],
        )
        email = payload.get("sub")  
        decrypt_email = decrypt_data(email)
   
        if decrypt_email is None:
            raise credentials_exception  
        
        token_data = schema_login.TokenData(email=decrypt_email)
        
    except InvalidTokenError:
        raise credentials_exception  
    
    auth_user = db.query(models.Users).filter(models.Users.email == token_data.email).first()
    if auth_user is None:
        raise credentials_exception  
    
    return auth_user
        
async def get_current_active_user(
    current_user: Annotated[models.Users, Depends(get_current_user)],
): 
    if current_user.is_active == False:  
        raise HTTPException(status_code=400, detail="Inactive User")
    return current_user