from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import app.schemas.movies as schema_movie
import app.services.movies as services_movie
from app.dependecy import get_db

router = APIRouter(prefix="/v1/movies", tags=["users"])

@router.post("/", response_model=schema_movie.MoviesOut) 
def create_movie(movie_in: schema_movie.MoviesCreate, db: Session = Depends(get_db)):
    return services_movie.create_movie(db, movie_in)

@router.get("/", response_model=list[schema_movie.MoviesOut])
def read_movies(db: Session = Depends(get_db)):
    return services_movie.get_movies(db)