from pydantic import BaseModel
from typing import Optional

class WarehouseBase(BaseModel):
    name: str
    location: str
    capacity: int
    owner: str

class WarehouseCreate(WarehouseBase):
    user_id: int

class WarehouseUpdate(WarehouseBase):
    pass

class WarehouseOut(WarehouseBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
