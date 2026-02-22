from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import app.schemas.users as schema_users
import app.services.users as services_users
from app.dependecy import get_db


router = APIRouter(prefix="/v1/users", tags=["users"])

@router.post("/", response_model=schema_users.User) 
def create_users(create_in: schema_users.UserCreate, db: Session = Depends(get_db)):
    return services_users.create_user(db, create_in)

@router.get("/", response_model=list[schema_users.User])
def read_users(db: Session = Depends(get_db)):
    return services_users.get_users(db)
    
@router.post("/verify", response_model=schema_users.User)
def verify(create_in: schema_users.LoginUser,):
    return services_users.verify_password(create_in)