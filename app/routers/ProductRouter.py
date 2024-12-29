from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from typing import List
from services.ProductService import create_product, update_product, delete_product, get_all_products, get_product_by_id
from schemas.Product import ProductCreate, ProductUpdate, ProductResponse
from config.database import get_db
from dependencies.auth import get_current_user
from services.CloudinaryService import upload_file_to_cloudinary

router = APIRouter(prefix="/products", tags=["Products"])

@router.post("/", response_model=ProductResponse)
async def post_product(
    product: ProductCreate, 
    photo: UploadFile = File(...),  # Accept the photo as a file
    db: Session = Depends(get_db), 
    current_user: dict = Depends(get_current_user)  # Get the authenticated user
):
    # Upload the photo to Cloudinary
    photo_url = upload_file_to_cloudinary(photo)

    # Create the product using the authenticated user's ID
    farmer_id = current_user["id"]  # Assuming the user ID is available in the token payload
    product_with_photo = product.dict()
    product_with_photo["photo"] = photo_url  # Add the photo URL to the product data

    return create_product(db, ProductCreate(**product_with_photo), farmer_id)
