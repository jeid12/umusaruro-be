from sqlalchemy.orm import Session
from models.Subscription import Subscription
from datetime import datetime

def create_subscription(db: Session, start_date: datetime, end_date: datetime, fee: float, status: str, user_id: int):
    new_subscription = Subscription(
        start_date=start_date,
        end_date=end_date,
        fee=fee,
        status=status,
        user_id=user_id
    )
    db.add(new_subscription)
    db.commit()
    db.refresh(new_subscription)
    return new_subscription

def get_all_subscriptions(db: Session):
    return db.query(Subscription).all()

def get_subscription_by_id(db: Session, subscription_id: int):
    return db.query(Subscription).filter(Subscription.id == subscription_id).first()

def update_subscription(db: Session, subscription_id: int, updated_data: dict):
    subscription = db.query(Subscription).filter(Subscription.id == subscription_id).first()
    if subscription:
        for key, value in updated_data.items():
            setattr(subscription, key, value)
        db.commit()
        db.refresh(subscription)
    return subscription

def delete_subscription(db: Session, subscription_id: int):
    subscription = db.query(Subscription).filter(Subscription.id == subscription_id).first()
    if subscription:
        db.delete(subscription)
        db.commit()
    return subscription
