from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from uuid import UUID
import app.schemas.movies as MSchemas
import app.models.movies as models
import app.others.validations as validation

def get_movies(db:Session, skip, limit):
    return db.query(models.Movies).offset(skip).limit(limit).all()

def create_movies(db:Session, movies_data: MSchemas.MoviesCreate):
        new_movie = models.Movies(
        title = movies_data.title,
        synopsis = movies_data.synopsis,
        image = movies_data.image,
        duration = movies_data.duration,
        release = movies_data.release,
        )
    
        db.add(new_movie)
        db.commit()
        db.refresh(new_movie)
    
        jsonRes = jsonable_encoder(new_movie)
        return JSONResponse(jsonRes)

def update_movies(uId: UUID, update_Movie: MSchemas.MoviesUpdate, db:Session):
    
    updateMovie = db.query(models.Movies).filter(models.Movies.id == uId).first()
    validation.ExsistingMoviesValidation(updateMovie, "DE")
    
    update_data = {
        k: v for k, v in update_Movie.model_dump(exclude_unset=True).items()
        if v not in (None, "",'')
    }
    
    for key, value in update_data.items():
        setattr(updateMovie, key, value)
        
    db.commit()
    db.refresh(updateMovie)
    jsonres = jsonable_encoder(updateMovie)
    return JSONResponse(jsonres)

def delete_movies(uId: UUID, db:Session):
    
    deleteMovie = db.query(models.Movies).filter(models.Movies.id == uId).first()
    validation.ExsistingMoviesValidation(deleteMovie, "DE")
    
    db.delete(deleteMovie)
    db.commit()
    return {"message": "Delete Movie Successfully"}