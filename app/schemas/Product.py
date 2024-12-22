from pydantic import BaseModel
from typing import Optional

# Pydantic schema for the Product
class ProductBase(BaseModel):
    name: str  # product name
    type: str  # product type (e.g., dairy, vegetables)
    price: float  # product price
    quantity: int  # available quantity of the product
    # farmer_id: int  # ID of the farmer (user) who owns the product

    class Config:
        orm_mode = True  # Allow Pydantic to work with SQLAlchemy models


class ProductCreate(ProductBase):
    pass  # This schema is used for creating new products


class ProductUpdate(ProductBase):
    name: Optional[str]  # Name is optional for update
    type: Optional[str]  # Type is optional for update
    price: Optional[float]  # Price is optional for update
    quantity: Optional[int]  # Quantity is optional for update


class ProductResponse(ProductBase):
    id: int  # The id will be included in the response after the product is created
    farmer_id: int  # ID of the farmer (user) who owns the product

    class Config:
        orm_mode = True  # This allows Pydantic to work seamlessly with SQLAlchemy models

