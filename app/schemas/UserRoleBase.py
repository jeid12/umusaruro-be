# schemas.py

from pydantic import BaseModel

class UserRoleBase(BaseModel):
    name: str

class UserRoleCreate(UserRoleBase):
    pass

class UserRoleResponse(UserRoleBase):
    id: int

    class Config:
        orm_mode = True
