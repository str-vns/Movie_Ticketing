from sqlalchemy import Column, String, DateTime, func, Boolean
from app.db.database import Base
import uuid

class Users(Base):
    __tablename__ = "users"
    
    id = Column(String, primary_key=True, default=uuid.uuid4, nullable=False)
    email = Column(String, index=True, nullable=False, unique=True)
    password = Column(String, nullable=False)
    firstName = Column(String, nullable=False, index=True)
    lastName = Column(String, nullable=False, index=True)
    pfp = Column(String,nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    