from sqlalchemy.orm import Session
from pwdlib import PasswordHash
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from uuid import UUID
import app.schemas.users as UsSchemas
import app.models.users as models
import app.others.validations as validation

password_hash = PasswordHash.recommended()

def get_users(db:Session, skip, limit):
    users = db.query(
        models.Users.id,
        models.Users.firstName, 
        models.Users.pfp, 
        models.Users.lastName,
        models.Users.email,
        models.Users.is_active
        
    ).offset(skip).limit(limit).all()

    if not users:
        raise HTTPException(status_code=404, detail="No users found")

    result = [
        {
            "id": str(user.id),
            "firstName": user.firstName,
            "lastName": user.lastName,
            "email": user.email,
            "pfp": user.pfp,
            "is_active": user.is_active
        }
        for user in users
    ]
    return JSONResponse(content=result)

def create_user(db:Session, user_data: UsSchemas.UserCreate):

    email_user = db.query(models.Users).filter(models.Users.email == user_data.email).first()
    validation.emailValidation(email_user)
    
    new_user = models.Users(
        firstName = user_data.firstName,
        lastName = user_data.lastName,
        pfp = user_data.pfp,
        password = password_hash.hash(user_data.password),
        email = user_data.email,
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    jsonRes = jsonable_encoder(new_user)
    return JSONResponse(jsonRes)

def update_user(uId: UUID, user_update: UsSchemas.UserUpdate, db:Session):

    updateUser = db.query(models.Users).filter(models.Users.id == uId).first()
    validation.ExistingUserValidation(updateUser, "DE")
    
    update_data = {
        k: v for k, v in user_update.model_dump(exclude_unset=True).items()
        if v not in (None, "",'')
    }
    
    for key, value in update_data.items():
        setattr(updateUser, key, value)
        
    db.commit()
    db.refresh(updateUser)
    jsonRes = jsonable_encoder(updateUser)
    return JSONResponse(jsonRes)

def delete_user(uId: UUID, db:Session):
    
    deleteUser = db.query(models.Users).filter(models.Users.id == uId).first()
    validation.ExistingUserValidation(deleteUser, "DE")
    
    db.delete(deleteUser)
    db.commit()
    return {"Message": "Delete User Successfully" }
    
def profile(uId: UUID, db:Session):
    userProfile = db.query(models.Users.firstName, 
                           models.Users.pfp, 
                           models.Users.lastName,
                           models.Users.email
                           ).filter(models.Users.id == uId, models.Users.is_active == True).first()
    
    validation.ExistingUserValidation(userProfile, "DE")
    
    jsonRes = {
        "firstName": userProfile.firstName,
        "lastName": userProfile.lastName,
        "email": userProfile.email,
        "pfp": userProfile.pfp
    }

    return JSONResponse(content=jsonRes)

def create_payOp(pay_data: UsSchemas.PaymentCreate, db:Session):
    
    existing_user = db.query(models.Users).filter(models.Users.id == pay_data.userId).first()
    validation.ExistingUserValidation(existing_user, "DE")
    
    existing_payOp = db.query(models.PaymentOption).filter(models.PaymentOption.accountNum == pay_data.accountNum).first()   
    validation.paymentOpValidation(existing_payOp,"D")
    
    new_pay = models.PaymentOption(
        accountNum = pay_data.accountNum,
        accountName = pay_data.accountName,
        cvc = pay_data.cvc,
        exp = pay_data.exp,
        cardType = pay_data.cardType,
        cardBranch = pay_data.cardBranch,
        userId = pay_data.userId
    )
    
    db.add(new_pay)
    db.commit()
    db.refresh(new_pay)
    jsonRes = jsonable_encoder(new_pay)
    return JSONResponse(jsonRes)

def delete_payOp(uId: UUID, db:Session):
    existing_payOp = db.query(models.PaymentOption).filter(models.PaymentOption.id == uId).first()   
    validation.paymentOpValidation(existing_payOp, "DE")
    
    db.delete(existing_payOp)
    db.commit()
    return {"Message": "Delete Payment Option Successfully" }

def get_payOp(uId:UUID, db:Session, skip, limit):
    userPayOp = db.query(models.PaymentOption).filter(models.PaymentOption.userId == uId).offset(skip).limit(limit).all()
    validation.ExistingUserValidation(userPayOp, "DE")
    
    jsonRes = jsonable_encoder(userPayOp)
    return JSONResponse(jsonRes)

