from sqlalchemy import Column, BigInteger, String, Enum, Text, TIMESTAMP, Integer, func
from .database import Base

class Product(Base):
    __tablename__ = "products"

    product_id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    category = Column(Enum('finished', 'semi-finished', 'raw', name='category_enum'), nullable=False)
    description = Column(String(250))
    product_image = Column(Text)  # For storing image URL
    sku = Column(String(100), unique=True, nullable=False)
    unit_of_measure = Column(Enum('mtr', 'mm', 'ltr', 'ml', 'cm', 'mg', 'gm', 'unit', 'pack', name='uom_enum'), nullable=False)
    lead_time = Column(Integer, nullable=False)  # Lead time in days
    created_date = Column(TIMESTAMP, server_default=func.current_timestamp())
    updated_date = Column(TIMESTAMP, server_default=func.current_timestamp(), onupdate=func.current_timestamp()) 