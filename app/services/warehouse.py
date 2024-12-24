from sqlalchemy.orm import Session
from models.Warehouse import Warehouse
from schemas.Warehouse import WarehouseCreate, WarehouseUpdate

def create_warehouse(db: Session, warehouse: WarehouseCreate):
    db_warehouse = Warehouse(**warehouse.dict())
    db.add(db_warehouse)
    db.commit()
    db.refresh(db_warehouse)
    return db_warehouse

def get_warehouse(db: Session, warehouse_id: int):
    return db.query(Warehouse).filter(Warehouse.id == warehouse_id).first()

def get_warehouses(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Warehouse).offset(skip).limit(limit).all()

def update_warehouse(db: Session, warehouse_id: int, warehouse: WarehouseUpdate):
    db_warehouse = db.query(Warehouse).filter(Warehouse.id == warehouse_id).first()
    for key, value in warehouse.dict(exclude_unset=True).items():
        setattr(db_warehouse, key, value)
    db.commit()
    db.refresh(db_warehouse)
    return db_warehouse

def delete_warehouse(db: Session, warehouse_id: int):
    db_warehouse = db.query(Warehouse).filter(Warehouse.id == warehouse_id).first()
    if db_warehouse:
        db.delete(db_warehouse)
        db.commit()
    return db_warehouse
