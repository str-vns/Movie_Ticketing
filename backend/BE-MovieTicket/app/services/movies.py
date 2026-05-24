from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from uuid import UUID
import app.schemas.movies as MSchemas
import app.models.movies as models
import app.others.validations as validation

# Movie
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

# Movie Schedule
def get_movieSched(db:Session, skip, limit):
    return db.query(models.MoviesSched).offset(skip).limit(limit).all()

def get_singleMovieSched(uId: UUID, db:Session, skip, limit):
    return  db.query(models.MoviesSched).filter(models.MoviesSched.movieId == uId).all()

def create_movieSched(movies_data: MSchemas.MovieSchedCreate, db:Session):
    new_movieSched = models.MoviesSched(
        start_time = movies_data.start_time,
        end_time = movies_data.end_time,
        price = movies_data.price,
        date = movies_data.date,
        available_seat = movies_data.available_seat,
        total_seat = movies_data.total_seat,
        room_info = movies_data.room_info,
        movieId = movies_data.movieId,
        cinemaId = movies_data.cinemaId
        )
    
    db.add(new_movieSched)
    db.commit()
    db.refresh(new_movieSched)
    
    jsonRes = jsonable_encoder(new_movieSched)
    return JSONResponse(jsonRes)

def update_movieSched(uId: UUID, movie_data: MSchemas.MoviesSchedUpdate, db:Session):
    
    updateSchedMovie = db.query(models.MoviesSched).filter(models.MoviesSched.id == uId).first()
    validation.ExsistingSchedMovieValidation(updateSchedMovie, "DE")
    
    update_data = {
        k: v for k, v in movie_data.model_dump(exclude_unset=True).items()
        if v not in (None, "",'')
    }
    
    for key, value in update_data.items():
        setattr(updateSchedMovie, key, value)
        
    db.commit()
    db.refresh(updateSchedMovie)
    jsonres = jsonable_encoder(updateSchedMovie)
    return JSONResponse(jsonres)

def delete_moviesSched(uId: UUID, db:Session):
    
    deleteMovie = db.query(models.MoviesSched).filter(models.MoviesSched.id == uId).first()
    validation.ExsistingSchedMovieValidation(deleteMovie, "DE")
    
    db.delete(deleteMovie)
    db.commit()
    return {"message": "Delete Movie Successfully"}