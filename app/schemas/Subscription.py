from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from utils.Status import SubscriptionStatus as status


class SubscriptionBase(BaseModel):
    start_date: datetime
    end_date: datetime
    fee: float
    status: status
    user_id: int


class SubscriptionCreate(SubscriptionBase):
    pass  # Use this schema for creating new subscriptions


class SubscriptionUpdate(BaseModel):
    start_date: Optional[datetime]
    end_date: Optional[datetime]
    fee: Optional[float]
    status: status
    user_id: Optional[int]


class SubscriptionOut(SubscriptionBase):
    id: int

    class Config:
        orm_mode = True  # Enables compatibility with SQLAlchemy models
