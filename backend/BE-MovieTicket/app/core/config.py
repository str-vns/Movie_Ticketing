from decouple import config

class Settings:
    PROJECT_NAME: str = "BE MOVIE_TICKET"
    VERSION: str = "1.0.0"
    DATABASE: str = config("DATABASE")
    DEFAULT_LANG: str = "en"
    
settings = Settings()