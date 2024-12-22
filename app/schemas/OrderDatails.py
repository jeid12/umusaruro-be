from pydantic import BaseModel
from typing import List, Optional

# Pydantic schema for creating an OrderDetail (for POST requests)
class OrderDetailCreate(BaseModel):
    quantity: int
    subtotal: float
    order_id: int  # Foreign key to the Order model
    product_id: int  # Foreign key to the Product model

    class Config:
        orm_mode = True  # Allows Pydantic to read data from SQLAlchemy models

# Pydantic schema for the OrderDetail response (for GET requests)
class OrderDetailResponse(BaseModel):
    id: int
    quantity: int
    subtotal: float
    order_id: int
    product_id: int

    class Config:
        orm_mode = True  # Allows Pydantic to read data from SQLAlchemy models

# Optional: If you need a schema for the entire order with its details
class OrderResponseWithDetails(BaseModel):
    id: int
    total: float  # Total price for the order (if this is part of the Order model)
    order_details: List[OrderDetailResponse]  # List of OrderDetail objects

    class Config:
        orm_mode = True  # Allows Pydantic to read data from SQLAlchemy models
