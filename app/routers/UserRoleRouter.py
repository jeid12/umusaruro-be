from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.UserRole import Role  # Assuming you have a Role model in your models
from services.UserRoleService import create_user_role  # Your service function
from schemas.UserRoleBase import UserRoleCreate, UserRoleResponse
from config.database import get_db  # Your database session dependency

router = APIRouter()

@router.post("/roles/", response_model=UserRoleResponse)
def create_role(role: UserRoleCreate, db: Session = Depends(get_db)):
    db_role = create_user_role(db=db, role=role)
    if not db_role:
        raise HTTPException(status_code=400, detail="Role creation failed")
    return db_role
