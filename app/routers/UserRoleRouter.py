from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from models.UserRole import Role  # Assuming you have a Role model in your models
from services.UserRoleService import create_user_role  # Your service function
from schemas.UserRoleBase import UserRoleCreate, UserRoleResponse
from config.database import get_db  # Your database session dependency
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/roles", tags=["User Roles"])

@router.post("/", response_model=UserRoleResponse)
def create_role(role: UserRoleCreate, db: Session = Depends(get_db)):
    
    db_role = create_user_role(db=db, role=role)
    if not db_role:
        raise HTTPException(status_code=400, detail="Role creation failed")
    return db_role

@router.get("/", response_model=List[UserRoleResponse])
def get_roles(db: Session = Depends(get_db)):
    roles = db.query(Role).all()
    if not roles:
        raise HTTPException(status_code=404, detail="No roles found")
    return roles

@router.get("/{role_id}", response_model=UserRoleResponse)
def get_role_by_id(role_id: int, db: Session = Depends(get_db)):  
    role = db.query(Role).filter(Role.id == role_id).first()
    if not role:
        raise HTTPException(status_code=404, detail=f"Role with id {role_id} not found")
    return role 

@router.put("/{role_id}", response_model=UserRoleResponse)
def update_role(role_id: int, role: UserRoleCreate, db: Session = Depends(get_db)):
    db_role = db.query(Role).filter(Role.id == role_id).first()
    if not db_role:
        raise HTTPException(status_code=404, detail=f"Role with id {role_id} not found")
    db_role.name = role.name
    db.commit()
    db.refresh(db_role)
    return JSONResponse(content={"message": f"Role with id {role_id} updated successfully"}, status_code=200)

@router.delete("/{role_id}")
def delete_role(role_id: int, db: Session = Depends(get_db)):
    db_role = db.query(Role).filter(Role.id == role_id).first()
    if not db_role:
        raise HTTPException(status_code=404, detail=f"Role with id {role_id} not found")
    db.delete(db_role)
    db.commit()
    return JSONResponse(content={"message": f"Role with id {role_id} deleted successfully"}, status_code=200)  
