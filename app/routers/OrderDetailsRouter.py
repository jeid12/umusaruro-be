from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from services.OrderDetailsService import OrderDetailsService
from schemas.OrderDatails import OrderDetailCreate, OrderDetailResponse
from config.database import get_db  # Assuming you have a function to get a DB session

router = APIRouter(prefix="/order_details", tags=["Order Details"])

@router.post("/", response_model=OrderDetailResponse)
def create_order_detail(order_detail: OrderDetailCreate, db: Session = Depends(get_db)):
    return OrderDetailsService.create_order_detail(db=db, order_detail=order_detail)

@router.get("/{order_detail_id}", response_model=OrderDetailResponse)
def get_order_detail(order_detail_id: int, db: Session = Depends(get_db)):
    return OrderDetailsService.get_order_detail_by_id(db=db, order_detail_id=order_detail_id)

@router.get("/", response_model=List[OrderDetailResponse])
def get_order_details(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return OrderDetailsService.get_all_order_details(db=db, skip=skip, limit=limit)

@router.put("/{order_detail_id}", response_model=OrderDetailResponse)
def update_order_detail(order_detail_id: int, order_detail: OrderDetailCreate, db: Session = Depends(get_db)):
    return OrderDetailsService.update_order_detail(db=db, order_detail_id=order_detail_id, updated_order_detail=order_detail)

@router.delete("/{order_detail_id}")
def delete_order_detail(order_detail_id: int, db: Session = Depends(get_db)):
    return OrderDetailsService.delete_order_detail(db=db, order_detail_id=order_detail_id)
