from decouple import config
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
      app_name: str = "Movie Ticketing API"
    #   admin_email: str
      items_per_user: int = 50
    
    
settings = Settings()