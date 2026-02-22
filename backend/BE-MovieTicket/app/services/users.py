from sqlalchemy.orm import Session
from pwdlib import PasswordHash
import app.schemas.users as UsSchemas
import app.models.users as models

password_hash = PasswordHash.recommended()


def get_users(db:Session, skip=0, limit=10):
    return db.query(models.Users).offset(skip).limit(limit).all()

def create_user(db:Session, user_data: UsSchemas.UserCreate):
    
    new_user = models.Users(
        firstName = user_data.firstName,
        lastName = user_data.lastName,
        pfp = user_data.pfp,
        password = password_hash.hash(user_data.password),
        email = user_data.email,
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def verify_password(user_data: UsSchemas.LoginUser):
    print("test", user_data.password)
    if(password_hash.verify(user_data.password, "$argon2id$v=19$m=65536,t=3,p=4$CcM7Mi4Y1l60CgqnELk5Iw$HhOCdFrHJEg8CaRD2XrmIMeM+D4xh63zAJtJSiJCGk0")):
        print(True)
    else:
        print(False)

