from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional


SECRET_KEY = "1cf4c7087e140584b990966e024e6f7bc8557edf1ceb1d63a138a22e6fb96139dac7defcb7d5d36ac7b31e2736181627e6f07883c9ba7e19e2e45fd855a9ee78"  # You should store this securely in environment variables
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60  # You can adjust this as per your requirement

# Function to create an access token
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode = data.copy()
    to_encode.update({"exp": expire})
    
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Function to verify a JWT token and get the user email
def verify_jwt(token: str) -> Optional[str]:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            return None
        return email
    except JWTError:
        return None
