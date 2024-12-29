from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from typing import List
from services.ProductService import create_product, update_product, delete_product, get_all_products, get_product_by_id
from schemas.Product import ProductCreate, ProductUpdate, ProductResponse
from config.database import get_db
from dependencies.auth import get_current_user  # Dependency to get the current authenticated user
from services.CloudinaryService import upload_file_to_cloudinary  # Service to upload files to Cloudinary

router = APIRouter(prefix="/products", tags=["Products"])

@router.post("/", response_model=ProductResponse)
async def post_product(
    product: ProductCreate, 
    photo: UploadFile = File(...),  # Accept the photo as a file
    db: Session = Depends(get_db), 
    current_user: dict = Depends(get_current_user)  # Get the authenticated user from JWT
):
    # Upload the photo to Cloudinary
    photo_url = upload_file_to_cloudinary(photo)

    # Use the current user's ID to associate the product with the correct farmer
    farmer_id = current_user["id"]  # Assuming the user ID is available in the token payload
    
    # Add the photo URL to the product data
    product_with_photo = product.dict()
    product_with_photo["photo"] = photo_url  # Add the photo URL to the product data

    # Create the product using the farmer's ID
    return create_product(db, ProductCreate(**product_with_photo), farmer_id)


@router.put("/{product_id}", response_model=ProductResponse)
async def update_product(
    product_id: int, 
    product: ProductUpdate, 
    db: Session = Depends(get_db), 
    current_user: dict = Depends(get_current_user)  # Ensure the user is authenticated
):
    # Get the existing product from the database
    existing_product = db.query(Product).filter(Product.id == product_id).first()
    
    if not existing_product:
        raise HTTPException(status_code=404, detail="Product not found")

    if existing_product.farmer_id != current_user["id"]:
        raise HTTPException(status_code=403, detail="You do not have permission to update this product")

    return update_product(db, product_id, product)


@router.delete("/{product_id}", response_model=ProductResponse)
async def delete_product(
    product_id: int, 
    db: Session = Depends(get_db), 
    current_user: dict = Depends(get_current_user)  # Ensure the user is authenticated
):
    # Get the existing product from the database
    existing_product = db.query(Product).filter(Product.id == product_id).first()

    if not existing_product:
        raise HTTPException(status_code=404, detail="Product not found")

    if existing_product.farmer_id != current_user["id"]:
        raise HTTPException(status_code=403, detail="You do not have permission to delete this product")

    delete_product(db, product_id)
    return {"detail": "Product deleted successfully"}


@router.get("/", response_model=List[ProductResponse])
async def get_all_product(db: Session = Depends(get_db)):
    return get_all_products(db)


@router.get("/{product_id}", response_model=ProductResponse)
async def get_product_by_id(
    product_id: int, 
    db: Session = Depends(get_db)
):
    return get_product_by_id(db, product_id)
