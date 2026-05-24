from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from uuid import UUID
from app.dependecy import get_db
import app.core.auth as AUTH
import app.schemas.movies as schema_movie
import app.services.movies as services_movie
import app.models.users as model_users

router = APIRouter(prefix="/v1/movies", tags=["movies"])

@router.get("/", response_model=list[schema_movie.MoviesOut])
def read_movies(db: Session = Depends(get_db), skip=0, limit=10):
    return services_movie.get_movies(db, skip, limit)

@router.post("/", response_model=schema_movie.MoviesOut) 
def create_movie(movie_in: schema_movie.MoviesCreate, db: Session = Depends(get_db), current_user: model_users.Users = Depends(AUTH.get_current_user)):

    return services_movie.create_movies(db, movie_in)
    
@router.patch("/{uId}", response_model=schema_movie.MoviesOut)
def update_movie(uId: UUID, movie_data: schema_movie.MoviesUpdate, db: Session = Depends(get_db), current_user: model_users.Users = Depends(AUTH.get_current_user)):
    return services_movie.update_movies(uId, movie_data, db)

@router.delete("/{uId}", response_model=schema_movie.MoviesDelete)
def delete_movie(uId: UUID, db: Session = Depends(get_db), current_user: model_users.Users = Depends(AUTH.get_current_user)):
    return services_movie.delete_movies(uId, db)  

@router.get("/schedule", response_model=list[schema_movie.MovieScheds])
def read_movies(db:Session = Depends(get_db), skip=0, limit=10):
    return services_movie.get_movieSched(db, skip, limit)

@router.get("/{uId}/schedule", response_model=list[schema_movie.MovieScheds])
def read_singleMovies(uId: UUID, db:Session = Depends(get_db), skip=0, limit=0):
    return services_movie.get_singleMovieSched(uId, db, skip, limit)

@router.post("/schedule", response_model=schema_movie.MovieSchedCreate)
def create_sched(movie_sched: schema_movie.MovieSchedCreate, db:Session = Depends(get_db), current_user: model_users.Users = Depends(AUTH.get_current_user) ):
    return services_movie.create_movieSched(movie_sched, db)

@router.patch("/{uId}/schedule", response_model=schema_movie.MovieScheds)
def update_sched(uId: UUID, movie_data: schema_movie.MoviesSchedUpdate, db: Session = Depends(get_db), current_user: model_users.Users = Depends(AUTH.get_current_user)):
    return services_movie.update_movieSched(uId, movie_data, db)

@router.delete("/{uId}/schedule", response_model=schema_movie.MovieScheds)
def delete_sched(uId: UUID, db: Session = Depends(get_db), current_user: model_users.Users = Depends(AUTH.get_current_user)):
    return services_movie.delete_moviesSched(uId, db)  