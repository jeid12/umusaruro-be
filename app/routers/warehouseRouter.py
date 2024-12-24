from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.Warehouse import WarehouseCreate, WarehouseUpdate, WarehouseOut
from models.User import User
from services import warehouse as crud_warehouse
from config.database import get_db

router = APIRouter(prefix="/warehouses", tags=["Warehouses"])

@router.post("/", response_model=WarehouseOut)
def create_warehouse(warehouse: WarehouseCreate, db: Session = Depends(get_db)):
    return crud_warehouse.create_warehouse(db=db, warehouse=warehouse)

@router.get("/{warehouse_id}", response_model=WarehouseOut)
def get_warehouse(warehouse_id: int, db: Session = Depends(get_db)):
    db_warehouse = crud_warehouse.get_warehouse(db=db, warehouse_id=warehouse_id)
    if not db_warehouse:
        raise HTTPException(status_code=404, detail="Warehouse not found")
    return db_warehouse

@router.get("/", response_model=list[WarehouseOut])
def get_warehouses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud_warehouse.get_warehouses(db=db, skip=skip, limit=limit)

@router.put("/{warehouse_id}", response_model=WarehouseOut)
def update_warehouse(warehouse_id: int, warehouse: WarehouseUpdate, db: Session = Depends(get_db)):
    db_warehouse = crud_warehouse.get_warehouse(db=db, warehouse_id=warehouse_id)
    if not db_warehouse:
        raise HTTPException(status_code=404, detail="Warehouse not found")
    return crud_warehouse.update_warehouse(db=db, warehouse_id=warehouse_id, warehouse=warehouse)

@router.delete("/{warehouse_id}", response_model=WarehouseOut)
def delete_warehouse(warehouse_id: int, db: Session = Depends(get_db)):
    db_warehouse = crud_warehouse.get_warehouse(db=db, warehouse_id=warehouse_id)
    if not db_warehouse:
        raise HTTPException(status_code=404, detail="Warehouse not found")
    return crud_warehouse.delete_warehouse(db=db, warehouse_id=warehouse_id)
