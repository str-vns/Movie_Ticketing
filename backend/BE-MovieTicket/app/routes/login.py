from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependecy import get_db
import app.schemas.login as schema_login
import app.services.login as services_login
import app.models.users as model_users
import app.core.auth as AUTH

router = APIRouter(prefix="/v1", tags=["login"])

@router.post("/login", response_model=schema_login.Token)
def login_user(login_in: schema_login.UserLogin, db: Session = Depends(get_db)):
    user_data = services_login.authenticate_user(login_in, db)
    return user_data

@router.post("/generate-otp")
def generate_otp(email_input: schema_login.TokenData, db: Session = Depends(get_db)):
    return services_login.OTP_gen(email_input, db)
 
@router.post("/verify-otp")
def verify_otp(otp_input: schema_login.OTPRequest, db: Session = Depends(get_db)):
    return services_login.OTP_Verify(otp_input, db)

@router.post("/forgot-password")
def fp_pass(email_input: schema_login.TokenData, db: Session = Depends(get_db)):
    return services_login.Forget_password(email_input, db)

@router.patch("/reset-password")
def reset_password(forgotPass: schema_login.RESETPass, db: Session = Depends(get_db), current_user: model_users.Users = Depends(AUTH.get_current_user)):
    return services_login.reset_password(forgotPass, db, current_user)