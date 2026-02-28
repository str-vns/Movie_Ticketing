import os 
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from dotenv import load_dotenv
from cryptography.fernet import Fernet

load_dotenv()


origins = [
    os.getenv("Lk_Front"),
    os.getenv("LocalHost"),
    os.getenv("RedisHost")
]

ALLOW_METHODS = ["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"]
ALLOW_HEADERS = ["Authorization", "Content-type", "Accept", "Cookie"]

SECRET_KEY = os.getenv("FASTAPI_AES_KEY", "AES_KEY")
class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["Content-Security-Policy"] = "default-src 'self'; script-src 'self'; style-src 'self'; object-src 'none';"
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        return response

def setup_cors(app: FastAPI):
   app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=ALLOW_METHODS,
    allow_headers=ALLOW_HEADERS
    )
    
def setup_http(app: FastAPI):
    app.add_middleware(
        SecurityHeadersMiddleware,
    )
    
f = Fernet(SECRET_KEY)

def encrypt_data(data: str) -> str:
    
    encrypted_data = f.encrypt(data.encode())
    return encrypted_data.decode()

def decrypt_data(encrypted_data: str) -> str:
    decrypted_data = f.decrypt(encrypted_data.encode())
    print("Decrypted Data:", decrypted_data)
    return decrypted_data.decode()
