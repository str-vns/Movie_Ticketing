from sqlalchemy import Column, String, DateTime, func, Boolean, ForeignKey
from app.db.database import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
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
    # delete_exp = Column(DateTime(timezone=True))
    paymentOp = relationship("PaymentOption", back_populates="userInfo")

class PaymentOption(Base):
    __tablename__ = "paymentoptions"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4 )
    accountNum = Column(String, index=True, nullable=False, unique=True)
    accountName = Column(String, nullable=True)
    cvc = Column(String, nullable=True)
    exp = Column(String, nullable=True)
    cardType = Column(String,nullable=False)
    cardBranch = Column(String, nullable=False)
    userId = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    userInfo = relationship("Users", back_populates="paymentOp")
    created_at = Column(DateTime(timezone=True), server_default=func.now())