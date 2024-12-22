from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base  # Assuming you have a Base class defined for SQLAlchemy models

class OrderDetail(Base):
    __tablename__ = 'order_details'  # Define the table name

    id = Column(Integer, primary_key=True, autoincrement=True)  # Primary key
    quantity = Column(Integer, nullable=False)  # Quantity of the product in the order
    subtotal = Column(Float, nullable=False)  # Subtotal for the order detail (quantity * price)
    
    # Foreign keys linking to the Order and Product tables
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)

    # Relationship fields for easy access to related data
    order = relationship('Order', back_populates='order_details')  # Assuming Order model has a relationship with OrderDetail
    product = relationship('Product', back_populates='order_details')  # Assuming Product model has a relationship with OrderDetail
