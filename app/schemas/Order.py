from pydantic import BaseModel
from datetime import datetime
from enum import Enum
from typing import Optional
from utils.Status import OrderStatus

class OrderBase(BaseModel):
    delivery_address: str
    status: OrderStatus = OrderStatus.PENDING  # Default value
    client_id: int

class OrderCreate(OrderBase):
    pass


class OrderRead(OrderBase):
    id: int
    order_date: datetime

    class Config:
        orm_mode = True

class OrderUpdate(BaseModel):
    
    status: Optional[OrderStatus] = None
    
