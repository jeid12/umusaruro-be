from sqlalchemy.orm import Session
from fastapi import HTTPException
from typing import List
from models.Product import Product  # SQLAlchemy Product model
from schemas.Product import ProductCreate, ProductUpdate, ProductResponse

# Create a new product
def create_product(db: Session, product: ProductCreate) -> ProductResponse:
    db_product = Product(**product.dict())  # Create a new Product object
    db.add(db_product)
    db.commit()  # Commit the transaction to the database
    db.refresh(db_product)  # Refresh to get the updated data (e.g., auto-generated ID)
    return ProductResponse.from_orm(db_product)


# Update an existing product
def update_product(db: Session, product_id: int, product: ProductUpdate) -> ProductResponse:
    db_product = db.query(Product).filter(Product.id == product_id).first()  # Query product by ID
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")

    # Update product fields with the provided data (excluding unset fields)
    for field, value in product.dict(exclude_unset=True).items():
        setattr(db_product, field, value)

    db.commit()  # Commit changes to the database
    db.refresh(db_product)  # Refresh the product instance with the latest data
    return ProductResponse.from_orm(db_product)


# Delete a product
def delete_product(db: Session, product_id: int) -> None:
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    db.delete(db_product)  # Mark the product for deletion
    db.commit()  # Commit the deletion to the database


# Get all products
def get_all_products(db: Session) -> List[ProductResponse]:
    products = db.query(Product).all()  # Retrieve all products from the database
    return [ProductResponse.from_orm(product) for product in products]


# Get a product by ID
def get_product_by_id(db: Session, product_id: int) -> ProductResponse:
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return ProductResponse.from_orm(db_product)
