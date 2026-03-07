from sqlalchemy import Column, String, DateTime, func, Boolean
from app.db.database import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Users(Base):
    __tablename__ = "users"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4 )
    email = Column(String, index=True, nullable=False, unique=True)
    password = Column(String, nullable=False)
    firstName = Column(String, nullable=False, index=True)
    lastName = Column(String, nullable=False, index=True)
    pfp = Column(String,nullable=True)
    role = Column(String, default="consumer")
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    