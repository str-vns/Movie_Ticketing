from sqlalchemy.orm import Session
import app.schemas.movies as MSchemas
import app.models.movies as models

def get_movies(db:Session, skip=0, limit=10):
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
    return new_movie