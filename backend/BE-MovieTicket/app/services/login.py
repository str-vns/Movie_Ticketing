import os
from sqlalchemy.orm import Session
from pwdlib import PasswordHash
from fastapi import HTTPException, status
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
import app.schemas.login as schema_login
import app.models.users as models
import app.core.auth as auth
from app.core.security import encrypt_data

load_dotenv()

password_hash = PasswordHash.recommended()

def authenticate_user(login_data: schema_login.UserLogin, db: Session):
    authUser = db.query(models.Users).filter(models.Users.email == login_data.email).first()
    if not authUser:
       raise HTTPException(
        status_code=400,
        detail="This User does not Exist"
    ) 
    elif authUser.is_active == False :
        raise HTTPException(
        status_code=400,
        detail="This User is Inactive PLEASE Contact the Admin"
    )
        
    if password_hash.verify(login_data.password, authUser.password):
       access_token_expires = timedelta(minutes=int(os.getenv("ATEM", 60)))
       
       encrpyEmail = encrypt_data(authUser.email)
       access_token = auth.create_access_token(
           data={"sub": encrpyEmail},
           expires_delta=access_token_expires,
       )
       
       return schema_login.Token(access_token=access_token, token_type="Bearer", accessDay=datetime.now(timezone.utc), expireDay=datetime.now(timezone.utc) + access_token_expires, User={
              "id": str(authUser.id),
              "firstName": authUser.firstName,
              "lastName": authUser.lastName,
              "email": authUser.email,
              "pfp": authUser.pfp
         })
    else:
       raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    
   