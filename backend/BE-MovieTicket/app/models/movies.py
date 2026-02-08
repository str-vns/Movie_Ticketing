from sqlalchemy import Column, String, DateTime, func, Boolean
from app.db.database import Base
import uuid

class Movies(Base):
    __tablename__ = "movies"
    
    id = Column(String, primary_key=True, default=uuid.uuid4, nullable=False)
    title = Column(String(255), index=True, nullable=False)
    synopsis = Column(String, nullable=True)
    image = Column(String, nullable=False)
    duration = Column(String, nullable=False)
    release = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    is_delete = Column(Boolean, default=False)
    
    
    
    
    
    