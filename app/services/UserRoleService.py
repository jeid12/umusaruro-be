from sqlalchemy.orm import Session
from models.UserRole import Role
from schemas.UserRoleBase import UserRoleCreate

def create_user_role(db: Session, role: UserRoleCreate):
    # Check if role with the same name already exists
    db_role = db.query(Role).filter(Role.name == role.name).first()
    if db_role:
        return db_role  # or raise an exception if role already exists
    
    # If role doesn't exist, create it
    new_role = Role(name=role.name)
    db.add(new_role)
    db.commit()
    db.refresh(new_role)
    
    return new_role

