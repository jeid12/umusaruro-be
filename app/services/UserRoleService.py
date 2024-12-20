from sqlalchemy.orm import Session
from models.UserRole import Role
from schemas.UserRoleBase import UserRoleCreate

def create_user_role(db: Session, role: UserRoleCreate):
    db_role = Role(name=role.name)
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role
