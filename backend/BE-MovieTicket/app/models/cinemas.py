from sqlalchemy import Column, String, DateTime, func, Boolean, Time, ForeignKey
from app.db.database import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Cinemas(Base):
    __tablename__ = "cinemas"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    cinemaName = Column(String(255), index=True, nullable=False)
    cinemaAddress = Column(String, nullable=True)
    cinemaOpen = Column(Time, nullable=False)
    cinemaClose = Column(Time, nullable=False)
    cinemaSched = Column(String, nullable=False)
    cinema_x = Column(String, nullable=False)
    cinema_y = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    delete_exp = Column(DateTime(timezone=True))
    is_delete = Column(Boolean, default=False)
    
class Rooms(Base):
    __tablename__ = "rooms"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    roomInfo = Column(String, index=True, nullable=False)
    cinemaId = Column(UUID(as_uuid=True), ForeignKey("cinemas.id"))
    status = Column(String(), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    delete_exp = Column(DateTime(timezone=True))
    is_delete = Column(Boolean, default=False)   

  
    
    
        