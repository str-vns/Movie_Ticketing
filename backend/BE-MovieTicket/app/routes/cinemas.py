from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from uuid import UUID
from app.dependecy import get_db
import app.core.auth as AUTH
import app.schemas.cinemas as schema_cinema
import app.services.cinemas as services_cinema
import app.models.users as model_users

router = APIRouter(prefix="/v1/cinema", tags=["cinema"])

@router.get("/", response_model=list[schema_cinema.CinemasOut])
def read_cinema(db: Session = Depends(get_db), skip=0, limit=10):
    return services_cinema.get_cinemas(db, skip, limit)

@router.post("/", response_model=schema_cinema.CinemasCreate) 
def create_cinema(cinema_in: schema_cinema.CinemasCreate, db: Session = Depends(get_db), current_user: model_users.Users = Depends(AUTH.get_current_user)):
    return services_cinema.create_cinemas(db, cinema_in)
    
@router.patch("/{uId}", response_model=schema_cinema.CinemasUpdate)
def update_cinema(
    uId: str,
    cinema_data: schema_cinema.CinemasUpdate, 
    db: Session = Depends(get_db),
    current_user: model_users.Users = Depends(AUTH.get_current_user)
):
    return services_cinema.update_cinemas(db, uId, cinema_data)

@router.delete("/{uId}", response_model=schema_cinema.CinemasDelete)
def delete_einema(uId: UUID, db: Session = Depends(get_db), current_user: model_users.Users = Depends(AUTH.get_current_user)):
    return services_cinema.delete_einema(uId, db)  

