import os
from sqlalchemy.orm import Session
from pwdlib import PasswordHash
from fastapi import HTTPException, status
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
from app.core.security import encrypt_data
from datetime import datetime, timedelta
import app.models.otp as otps
import app.schemas.login as schema_login
import app.models.users as models
import app.core.auth as auth
import app.others.emailGenerate as emailG
import pyotp


load_dotenv()

password_hash = PasswordHash.recommended()

def generate_otp_secret():
    return pyotp.random_base32()

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

def OTP_gen(email_input, db):
    otp_secret = generate_otp_secret()
    email = email_input.email
    totp = pyotp.TOTP(otp_secret)
    otp = totp.now()
    expires = datetime.now(timezone.utc) + timedelta(minutes=3)
    
    otp_record = otps.OTP(
        email=email,
        otp_code=otp,
        expires_at=expires
    )
    
    db.add(otp_record)
    db.commit()
    
    emailG.send_email(email, "Your OTP CODE", f"Your OTP code is: {otp}")
    
    return {"email": email, "otp": otp}

def OTP_Verify(otp_input, db):

    otpVerify = db.query(otps.OTP).filter(otps.OTP.otp_code == otp_input.otp, otps.OTP.email == otp_input.email, otps.OTP.is_used == False).first()
    if not otpVerify:
        raise HTTPException(
            status_code=400,
            detail="Invalid Code"
        )
    
    if otpVerify.expires_at < datetime.now(timezone.utc):
        db.query(otps.OTP).filter(otps.OTP.expires_at < datetime.now(timezone.utc)).delete()
        db.commit()


        raise HTTPException(status_code=400, detail="OTP expired")
    
    otpVerify.is_used = True
    db.commit()
  
    return {"Message:"" SuccessFully login"}

def Forget_password(email_input, db):
    try: 
     authUser = db.query(models.Users).filter(models.Users.email == email_input.email).first()
     if authUser is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                  detail="Invalid Email address")
     encrpyEmail = encrypt_data(authUser.email)
     access_token = auth.create_access_token(
           data={"sub": encrpyEmail},
           expires_delta=timedelta(minutes=10),
       )
    
    
     forget_url_link = f"{access_token}"
    
     emailG.send_email(authUser.email, "Your Reset Link", f"Your Link is: {forget_url_link}")    
    
     
     return {"send email successfully"}
    except Exception as e:
           raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
              detail=f"Something Unexpected, Server Error {e}")
    
def reset_password(forgotPass, db, Cu):
    
    print(f"c{Cu.id}")
    if (forgotPass.new_password != forgotPass.confirm_password):
       raise HTTPException(
        status_code=400,
        detail="New Password and Confirm Password are not same"
    ) 
    hashed_pass = password_hash.hash(forgotPass.confirm_password)
    user = db.query(models.Users).filter(models.Users.id == Cu.id).first()   
    
    if not user:
       raise HTTPException(
        status_code=400,
        detail="This User does not Exist"
    ) 
    
    user.password = hashed_pass
    db.commit()
    
        
    return {"message": "Password updated successfully"}    
    