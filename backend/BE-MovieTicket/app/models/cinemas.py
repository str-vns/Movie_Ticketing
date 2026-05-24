from sqlalchemy import Column, String, DateTime, func, Boolean, Time
from app.db.database import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Cinemas(Base):
    __tablename__ = "cinemas"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4 )
    cinemaName = Column(String(255), index=True, nullable=False)
    cinemaAddress = Column(String, nullable=True)
    cinemaOpen = Column(Time, nullable=False)
    cinemaClose = Column(Time, nullable=False)
    cinemaSched = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    is_delete = Column(Boolean, default=False)