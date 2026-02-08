from fastapi import FastAPI
from app.routes import movies
from app.db.database import Base, engine

Base.metadata.create_all(bind=engine)
    
app = FastAPI()
app.include_router(movies.router)

    
