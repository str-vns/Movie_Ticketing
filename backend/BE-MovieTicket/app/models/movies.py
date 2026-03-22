from sqlalchemy import Column, String, DateTime, func, Boolean
from app.db.database import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Movies(Base):
    __tablename__ = "movies"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4 )
    title = Column(String(255), index=True, nullable=False)
    synopsis = Column(String, nullable=True)
    image = Column(String, nullable=False)
    duration = Column(String, nullable=False)
    release = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    is_delete = Column(Boolean, default=False)
    
    
    
    
    
    