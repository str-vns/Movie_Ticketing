from sqlalchemy import Column, String, DateTime, func, Boolean, Float, Integer, ForeignKey
from app.db.database import Base
from sqlalchemy.dialects.postgresql import UUID
import app.models.cinemas as Mcinemas
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
    
class MoviesSched(Base):
    __tablename__ =  "moviessched" 
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4 )
    start_time = Column(String, nullable=False)
    end_time = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    available_seat = Column(Integer, nullable=False)
    total_seat = Column(Integer, nullable=False)
    room_info = Column(String, nullable=False)
    date = Column(String, nullable=False)
    movieId = Column(UUID(as_uuid=True), ForeignKey("movies.id"))
    cinemaId = Column(UUID(as_uuid=True), ForeignKey("cinemas.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    is_delete = Column(Boolean, default=False)
    
    
    