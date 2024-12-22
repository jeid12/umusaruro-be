from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from config.database import get_db
from schemas.Order import OrderCreate, OrderRead, OrderUpdate
from services.OrderService import create_order, get_all_orders, get_order_by_id, update_order, delete_order

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.post("", response_model=OrderRead)
def create_order_route(order_data: OrderCreate, db: Session = Depends(get_db)):
    return create_order(order_data, db)


@router.get("", response_model=List[OrderRead])
def get_all_orders_route(db: Session = Depends(get_db)):
    return get_all_orders(db)


@router.get("/{order_id}", response_model=OrderRead)
def get_order_route(order_id: int, db: Session = Depends(get_db)):
    return get_order_by_id(order_id, db)


@router.patch("/{order_id}", response_model=OrderRead)
def update_order_route(order_id: int, order_data: OrderUpdate, db: Session = Depends(get_db)):
    return update_order(order_id, order_data, db)


@router.delete("/{order_id}")
def delete_order_route(order_id: int, db: Session = Depends(get_db)):
    return delete_order(order_id, db)
