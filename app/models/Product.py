from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base  # Assuming you have a Base class defined for SQLAlchemy models

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)  # id field, primary key, auto-incremented
    name = Column(String, nullable=False)  # product name
    type = Column(String, nullable=False)  # product type (e.g., dairy, vegetables)
    price = Column(Float, nullable=False)  # product price
    quantity = Column(Integer, nullable=False)  # available quantity of the product
    farmer_id = Column(Integer, ForeignKey('users.id'), nullable=False)  # foreign key linking to the User table
    photo_url = Column(String, nullable=True)  # URL to the product photo

    # Relationships
    farmer = relationship('User', back_populates='products')  # Assuming User model has a relationship with Product
    order_details = relationship('OrderDetail', back_populates='product')  # Relationship with OrderDetail
