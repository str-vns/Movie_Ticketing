from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from uuid import UUID
import app.schemas.cinemas as CSchemas
import app.models.cinemas as models
import app.others.validations as validation

def get_cinemas(db:Session, skip, limit):
    return db.query(models.Cinemas).offset(skip).limit(limit).all()

def create_cinemas(db:Session, cinemas_data: CSchemas.CinemasCreate):
    
        new_cinemas = models.Cinemas(
        cinemaName = cinemas_data.cinemaName,
        cinemaAddress = cinemas_data.cinemaAddress,
        cinemaOpen = cinemas_data.cinemaOpen,
        cinemaClose = cinemas_data.cinemaClose,
        cinemaSched = cinemas_data.cinemaSched,
        )
    
        db.add(new_cinemas)
        db.commit()
        db.refresh(new_cinemas)
    
        jsonRes = jsonable_encoder(new_cinemas)
        return JSONResponse(jsonRes)

def update_cinemas(uId: UUID, update_Cinema: CSchemas.CinemasUpdate, db:Session):
    
    updateCinema= db.query(models.Cinemas).filter(models.Cinemas.id == uId).first()
    validation.ExsistingCinemasValidation(updateCinema, "DE")
    
    update_data = {
        k: v for k, v in update_Cinema.model_dump(exclude_unset=True).items()
        if v not in (None, "",'')
    }
    
    for key, value in update_data.items():
        setattr(updateCinema, key, value)
        
    db.commit()
    db.refresh(updateCinema)
    jsonres = jsonable_encoder(updateCinema)
    return JSONResponse(jsonres)

def delete_movies(uId: UUID, db:Session):
    
    deleteCinema= db.query(models.Cinemas).filter(models.Cinemas.id == uId).first()
    validation.ExsistingCinemasValidation(deleteCinema, "DE")
    
    db.delete(deleteCinema)
    db.commit()
    return {"message": "Delete Movie Successfully"}