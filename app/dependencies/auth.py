from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import timedelta
from config.database import get_db
from models.User import User
from schemas.User import UserLogin  # Assuming you have a UserLogin schema for login input
from utils.passwordHash import verify_password  # Import your password verification function
from services.jwt import create_access_token  # Function to create JWT tokens
from fastapi.security import OAuth2PasswordBearer

# Initialize the router for authentication-related endpoints
router = APIRouter(prefix="/auth", tags=["Auth"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

# Login Route
@router.post("/login")
async def login(user: UserLogin, db: Session = Depends(get_db)):
    # Fetch the user from the database based on email
    db_user = db.query(User).filter(User.email == user.email).first()
    
    if not db_user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    # Verify the provided password with the stored hashed password
    if not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    # Generate the JWT token for the user
    access_token_expires = timedelta(minutes=30)  # Set token expiration time
    access_token = create_access_token(data={"sub": db_user.email}, expires_delta=access_token_expires)
    
    # Create the response data manually
    response_data = {
        "access_token": access_token,
        "token_type": "bearer",
        "user": {
            "id": db_user.id,
            "name": db_user.name,
            "email": db_user.email,
            "contact": db_user.contact,
            "location": db_user.location,
            "role": db_user.role,
        }
    }
    
    return response_data


# Get Current User Route (protected by JWT)
@router.get("/users/me")
async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    # Verify and decode the JWT token
    user_email = verify_jwt(token)  # Use verify_jwt function to extract user info from token
    if user_email is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token or expired token")
    
    # Get the user based on the email from the token
    db_user = db.query(User).filter(User.email == user_email).first()
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    return {
        "id": db_user.id,
        "name": db_user.name,
        "email": db_user.email,
        "contact": db_user.contact,
        "location": db_user.location,
        "role": db_user.role,
    }
