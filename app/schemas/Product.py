from pydantic import BaseModel, HttpUrl
from typing import Optional


# Base schema for the Product
class ProductBase(BaseModel):
    name: str  # Product name
    type: str  # Product type (e.g., dairy, vegetables)
    price: float  # Product price
    quantity: int  # Available quantity of the product
    photo_url: Optional[HttpUrl] = None  # URL of the product photo (optional)

    class Config:
        orm_mode = True  # Allow Pydantic to work with SQLAlchemy models


# Schema for creating new products
class ProductCreate(ProductBase):
    farmer_id: int  # ID of the farmer (user) who owns the product


# Schema for updating products
class ProductUpdate(BaseModel):
    name: Optional[str] = None  # Name is optional for update
    type: Optional[str] = None  # Type is optional for update
    price: Optional[float] = None  # Price is optional for update
    quantity: Optional[int] = None  # Quantity is optional for update
    photo_url: Optional[HttpUrl] = None  # URL of the product photo (optional)


# Schema for product response
class ProductResponse(ProductBase):
    id: int  # The ID will be included in the response after the product is created
    farmer_id: int  # ID of the farmer (user) who owns the product
