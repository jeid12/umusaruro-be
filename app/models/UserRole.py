from sqlalchemy import Column, Integer, String
from config.database import Base
from sqlalchemy.orm import relationship

class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50), unique=True, index=True)

    users = relationship("User", back_populates="role")
