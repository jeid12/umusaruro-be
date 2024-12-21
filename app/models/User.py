
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(255))
    email = Column(String(255), unique=True,nullable=False)
    password = Column(String(255))
    contact = Column(String(255))
    location = Column(String(255))
    role_id = Column(Integer, ForeignKey('roles.id'))

    role = relationship("Role", back_populates="users")