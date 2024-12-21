
from sqlalchemy.orm import Session
from models.User import User
from schemas.User import UserCreate, UserUpdate
from utils.passwordHash import hash_password
from fastapi import HTTPException

def create_user(db: Session, user: UserCreate) -> User:
    """
    Create a new user in the database.
    """
    # Check if email already exists in the database
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Hash the password before saving it
    hashed_password = hash_password(user.password)
    
    # Create the user object
    new_user = User(
        name=user.name,
        email=user.email,
        contact=user.contact,
        location=user.location,
        role_id=user.role_id,
        password=hashed_password
    )
    
    # Add the user to the database and commit the transaction
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user


def get_all_users(db: Session):
    """
    Retrieve all users from the database.
    """
    users = db.query(User).all()
    if not users:
        raise HTTPException(status_code=404, detail="No users found")
    return users


def get_user_by_id(db: Session, user_id: int) -> User:
    """
    Retrieve a user by their ID from the database.
    """
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


def update_user(db: Session, user_id: int, user_update: UserUpdate) -> User:
    """
    Update an existing user's information.
    """
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Update user fields
    if user_update.name:
        user.name = user_update.name
    if user_update.contact:
        user.contact = user_update.contact
    if user_update.location:
        user.location = user_update.location
    if user_update.role_id:
        user.role_id = user_update.role_id
    if user_update.password:
        user.password = hash_password(user_update.password)
    
    # Commit changes to the database
    db.commit()
    db.refresh(user)
    
    return user


def delete_user(db: Session, user_id: int) -> str:
    """
    Delete a user from the database.
    """
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    db.delete(user)
    db.commit()
    
    return JSONResponse(content={"message": f"User with {user_id} deleted successfully"})
