
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from services.UserService import create_user, get_all_users, get_user_by_id, update_user, delete_user
from schemas.User import UserCreate, UserUpdate, UserResponse

from config.database import get_db

router = APIRouter(prefix="/users", tags=["Users"])



@router.post("/", response_model=UserResponse)
async def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Endpoint to create a new user in the database.
    """
    return create_user(db, user)

@router.get("/", response_model=List[UserResponse])
async def get_users(db: Session = Depends(get_db)):
    """
    Endpoint to retrieve all users from the database.
    """
    return get_all_users(db)

@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    """
    Endpoint to get user by their ID from the database.
    """
    return get_user_by_id(db, user_id)

@router.put("/{user_id}", response_model=UserResponse)
async def update_user_info(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    """
    Endpoint to update user information in the database.
    """
    return update_user(db, user_id, user_update)

@router.delete("/{user_id}")
async def delete_user_info(user_id: int, db: Session = Depends(get_db)):
    """
    Endpoint to delete a user from the database.
    """
    return delete_user(db, user_id)
