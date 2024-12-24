from sqlalchemy.orm import Session
from models.OrderDatails import OrderDetail  # Assuming your models are in the `models` directory
from schemas.OrderDatails import OrderDetailCreate, OrderDetailResponse  # Pydantic schemas
from fastapi import HTTPException, status

class OrderDetailsService:

    @staticmethod
    def create_order_detail(db: Session, order_detail: OrderDetailCreate):
        # Create a new order detail record
        db_order_detail = OrderDetail(
            quantity=order_detail.quantity,
            subtotal=order_detail.subtotal,
            order_id=order_detail.order_id,
            product_id=order_detail.product_id
        )
        db.add(db_order_detail)
        db.commit()
        db.refresh(db_order_detail)  # Refresh to get the new id
        return db_order_detail

    @staticmethod
    def get_order_detail_by_id(db: Session, order_detail_id: int):
        # Retrieve an order detail by its ID
        db_order_detail = db.query(OrderDetail).filter(OrderDetail.id == order_detail_id).first()
        if db_order_detail is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"OrderDetail with id {order_detail_id} not found"
            )
        return db_order_detail

    @staticmethod
    def get_all_order_details(db: Session, skip: int = 0, limit: int = 100):
        # Retrieve all order details with pagination support
        return db.query(OrderDetail).offset(skip).limit(limit).all()

    @staticmethod
    def update_order_detail(db: Session, order_detail_id: int, updated_order_detail: OrderDetailCreate):
        # Update an existing order detail
        db_order_detail = db.query(OrderDetail).filter(OrderDetail.id == order_detail_id).first()
        if db_order_detail is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"OrderDetail with id {order_detail_id} not found"
            )
        
        # Update the order detail fields
        db_order_detail.quantity = updated_order_detail.quantity
        db_order_detail.subtotal = updated_order_detail.subtotal
        db_order_detail.order_id = updated_order_detail.order_id
        db_order_detail.product_id = updated_order_detail.product_id

        db.commit()
        db.refresh(db_order_detail)
        return db_order_detail

    @staticmethod
    def delete_order_detail(db: Session, order_detail_id: int):
        # Delete an order detail
        db_order_detail = db.query(OrderDetail).filter(OrderDetail.id == order_detail_id).first()
        if db_order_detail is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"OrderDetail with id {order_detail_id} not found"
            )
        
        db.delete(db_order_detail)
        db.commit()
        return {"detail": "OrderDetail deleted successfully"}
