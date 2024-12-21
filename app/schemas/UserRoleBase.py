# schemas.py

from pydantic import BaseModel

class UserRoleBase(BaseModel):
    name: str

class UserRoleCreate(UserRoleBase):
    pass

class UserRoleResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
