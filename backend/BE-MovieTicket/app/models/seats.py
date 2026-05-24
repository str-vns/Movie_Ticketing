from sqlalchemy import Column, String, DateTime, func, Boolean, ForeignKey, Integer
from app.db.database import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Seats(Base):
    __tablename__ = "seats"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    roomId = Column(UUID(as_uuid=True), ForeignKey("rooms.id"))
    seat_num = Column(String, nullable=False)
    types = Column(String, nullable=False)
    row = Column(String, nullable=False)
    x_position = Column(Integer, nullable=False)
    y_position = Column(Integer, nullable=True)
    rotations = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    delete_exp = Column(DateTime(timezone=True))
    is_delete = Column(Boolean, default=False)

class SeatSched(Base):
    __tablename__ = "seatsSched"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    scheduleId = Column(UUID(as_uuid=True), ForeignKey("moviessched.id"))
    seatId = Column(UUID(as_uuid=True), ForeignKey("seats.id"))
    status = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    delete_exp = Column(DateTime(timezone=True))
    is_delete = Column(Boolean, default=False)