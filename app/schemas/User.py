# schemas/user.py
from pydantic import BaseModel
from typing import Optional
from schemas.UserRoleBase import Role  # Importing the Role schema

class UserBase(BaseModel):
    name: str
    email: str
    password: str
    contact: Optional[str] = None
    location: Optional[str] = None
    role_id: int

class UserLogin(BaseModel):
    email: str
    password: str


class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    name: Optional[str] = None
    contact: Optional[str] = None
    location: Optional[str] = None
    role_id: Optional[int] = None
    password: Optional[str] = None  

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    contact: str
    location: str
    role: Role

    class Config:
        orm_mode = True

class UserLoginResponse(BaseModel):
    id: int
    name: str
    email: str
    contact: str
    location: str
    role: Role
    access_token: str
    token_type: str

    class Config:
        orm_mode = True