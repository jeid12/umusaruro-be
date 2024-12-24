from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from config.database import get_db
from services.SubscriptionService import (
    create_subscription,
    get_all_subscriptions,
    get_subscription_by_id,
    update_subscription,
    delete_subscription,
)

router = APIRouter(prefix='/subscription',tags=['subscription'])

@router.post("/")
def add_subscription(start_date: str, end_date: str, fee: float, status: str, user_id: int, db: Session = Depends(get_db)):
    try:
        start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
        end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Use YYYY-MM-DD.")
    
    if start_date_obj > end_date_obj:
        raise HTTPException(status_code=400, detail="Start date must be before or equal to end date.")
    
    return create_subscription(db, start_date_obj, end_date_obj, fee, status, user_id)

@router.get("/")
def fetch_subscriptions(db: Session = Depends(get_db)):
    return get_all_subscriptions(db)

@router.get("/{subscription_id}")
def fetch_subscription_by_id(subscription_id: int, db: Session = Depends(get_db)):
    subscription = get_subscription_by_id(db, subscription_id)
    if not subscription:
        raise HTTPException(status_code=404, detail="Subscription not found.")
    return subscription

@router.put("/{subscription_id}")
def modify_subscription(subscription_id: int, updated_data: dict, db: Session = Depends(get_db)):
    subscription = update_subscription(db, subscription_id, updated_data)
    if not subscription:
        raise HTTPException(status_code=404, detail="Subscription not found.")
    return subscription

@router.delete("/{subscription_id}")
def remove_subscription(subscription_id: int, db: Session = Depends(get_db)):
    subscription = delete_subscription(db, subscription_id)
    if not subscription:
        raise HTTPException(status_code=404, detail="Subscription not found.")
    return {"detail": "Subscription deleted successfully"}
