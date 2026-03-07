from decouple import config
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Movie Ticketing API"
    # admin_email: str
    items_per_user: int = 50

    # security settings
    # SECRET_KEY and ALGORITHM are read from environment via decouple.
    # Using config() here ensures a clear error if the variable is missing.
    SECRET_KEY: str = config("SECRET_KEY")
    ALGORITHM: str = config("ALGO")


settings = Settings()