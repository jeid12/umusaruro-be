from tokenize import Double
from typing import Optional
from sqlalchemy import Column, Integer, Enum, String, String
from config.database import Base
from sqlalchemy import DateTime
from utils.Status import SubscriptionStatus as status

class Subscription(Base):
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True, index=True)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    fee = Column(Integer, nullable=False)
    status = Column(Enum(status), default=status.SUSPENDED, nullable=False)
    user_id = Column(Integer, nullable=False)
    
    
