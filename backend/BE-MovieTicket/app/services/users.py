from sqlalchemy.orm import Session
from pwdlib import PasswordHash
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from uuid import UUID
import app.schemas.users as UsSchemas
import app.models.users as models

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

    existing_user = db.query(models.Users).filter(models.Users.email == user_data.email).first()
    if existing_user:
       raise HTTPException(
        status_code=400,
        detail="Email already registered"
    )

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
    if not updateUser:
       raise HTTPException(
        status_code=400,
        detail="This User does not Exist"
    )
    
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
    if not deleteUser:
       raise HTTPException(
        status_code=400,
        detail="This User does not Exist"
    )
    
    db.delete(deleteUser)
    db.commit()
    return {"Message": "Delete User Successfully" }
    
def profile(uId: UUID, db:Session):
    userProfile = db.query(models.Users.firstName, 
                           models.Users.pfp, 
                           models.Users.lastName,
                           models.Users.email
                           ).filter(models.Users.id == uId, models.Users.is_active == True).first()
    if not userProfile:
        raise HTTPException(
        status_code=400,
        detail="This User does not Exist"
    ) 
    
    jsonRes = {
        "firstName": userProfile.firstName,
        "lastName": userProfile.lastName,
        "email": userProfile.email,
        "pfp": userProfile.pfp
    }

    return JSONResponse(content=jsonRes)