from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.Order import Order
from schemas.Order import OrderCreate, OrderUpdate
from typing import List


def create_order(order_data: OrderCreate, db: Session) -> Order:
    """
    Create a new order.
    """
    new_order = Order(**order_data.dict())
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order


def get_all_orders(db: Session) -> List[Order]:
    """
    Retrieve all orders.
    """
    if not db.query(Order).all():
        raise HTTPException(status_code=404, detail="No orders found")
    return db.query(Order).all()


def get_order_by_id(order_id: int, db: Session) -> Order:
    """
    Retrieve a single order by ID.
    """
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


def update_order(order_id: int, order_data: OrderUpdate, db: Session) -> Order:
    """
    Update an existing order.
    """
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    
    for field, value in order_data.dict(exclude_unset=True).items():
        setattr(order, field, value)
    
    db.commit()
    db.refresh(order)
    return order


def delete_order(order_id: int, db: Session) -> dict:
    """
    Delete an order by ID.
    """
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    
    db.delete(order)
    db.commit()
    return {"message": f"Order with ID {order_id} has been deleted successfully."}
