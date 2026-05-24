from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependecy import get_db
from uuid import UUID
import app.schemas.users as schema_users
import app.services.users as services_users
import app.models.users as model_users
import app.core.auth as AUTH

router = APIRouter(prefix="/v1/users", tags=["users"])

@router.post("/", response_model=schema_users.User) 
def create_users(create_in: schema_users.UserCreate, db: Session = Depends(get_db)):
    return services_users.create_user(db, create_in)

@router.get("/", response_model=list[schema_users.User])
def read_users(db: Session = Depends(get_db), skip: int=0, limit: int = 10, current_user: model_users.Users = Depends(AUTH.get_current_user)):
    return services_users.get_users(db, skip, limit )

@router.patch("/{uId}", response_model=schema_users.User)
def update_users(uId: UUID, user: schema_users.UserUpdate, db: Session = Depends(get_db), current_user: model_users.Users = Depends(AUTH.get_current_user)):
    return services_users.update_user(uId, user, db)
  
@router.delete("/{uId}", response_model=schema_users.User)
def delete_users(uId: UUID, db: Session = Depends(get_db), current_user: model_users.Users = Depends(AUTH.get_current_user)):
    return services_users.delete_user(uId,db)  

@router.get("/{uId}/profile", response_model=schema_users.User)
def profile_users(uId: UUID, db: Session = Depends(get_db), current_user: model_users.Users = Depends(AUTH.get_current_user)):
    return services_users.profile(uId, db)

@router.post("/payOption",  response_model=schema_users.PaymentCreate)
def create_payOp(create_pay: schema_users.PaymentCreate, db: Session = Depends(get_db), current_user: model_users.Users = Depends(AUTH.get_current_user)):
    return services_users.create_payOp(create_pay, db)

@router.delete("/payOption/{uId}")
def delete_payOP(uId: UUID, db: Session = Depends(get_db), current_user: model_users.Users = Depends(AUTH.get_current_user)):
    return services_users.delete_payOp(uId, db)

@router.get("/payOption/{uId}")
def get_payOp(uId: UUID, db: Session = Depends(get_db), skip: int=0, limit: int = 10, current_user: model_users.Users = Depends(AUTH.get_current_user)):
    return services_users.get_payOp(uId, db, skip, limit)