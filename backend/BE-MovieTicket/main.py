from fastapi import FastAPI, Depends
from functools import lru_cache
from app.routes import movies, users
from app.db.database import Base, engine
from app.core import config, security, limiter

Base.metadata.create_all(bind=engine)

app = FastAPI(
    # dependencies=[Depends(limiter.total_limiter), Depends(limiter.ip_limiter)]
)

@lru_cache
def get_settings():
    return config.Settings()

security.setup_cors(app)
security.setup_http(app)

app.include_router(movies.router)
app.include_router(users.router)

    
