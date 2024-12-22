from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum
from utils.Status import OrderStatus
from sqlalchemy.orm import relationship
from config.database import Base
from datetime import datetime


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    order_date = Column(DateTime, default=datetime.utcnow)  # Default to the current datetime
    delivery_address = Column(String(255))
    status = Column(Enum(OrderStatus), default=OrderStatus.PENDING)  # Enum column with default
    client_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    client = relationship("User", back_populates="orders")
