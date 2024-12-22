from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from services.ProductService import  create_product, update_product, delete_product, get_all_products, get_product_by_id
from schemas.Product import ProductCreate, ProductUpdate, ProductResponse  
from config.database import get_db  

router = APIRouter(prefix="/products", tags=["Products"])

@router.post("/", response_model=ProductResponse)
async def post_product(product: ProductCreate, db: Session = Depends(get_db)):
    # Assuming `farmer_id` is extracted from the authenticated user's data
    farmer_id = 2 # Replace with actual authentication logic
    return create_product(db, product, farmer_id)


@router.put("/{product_id}", response_model=ProductResponse)
async def updateproduct(product_id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    return update_product(db, product_id, product)


@router.delete("/{product_id}", response_model=ProductResponse)
async def deleteproduct(product_id: int, db: Session = Depends(get_db)):
    delete_product(db, product_id)
    return {"detail": "Product deleted successfully"}


@router.get("/", response_model=List[ProductResponse])
async def get_all_pro(db: Session = Depends(get_db)):
    return get_all_products(db)


@router.get("/{product_id}", response_model=ProductResponse)
async def get_by_id(product_id: int, db: Session = Depends(get_db)):
    return get_product_by_id(db, product_id)
