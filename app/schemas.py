from pydantic import BaseModel, Field
from typing import Optional, Literal
from datetime import datetime

class ProductBase(BaseModel):
    name: str = Field(..., max_length=100)
    category: Literal['finished', 'semi-finished', 'raw']
    description: Optional[str] = Field(None, max_length=250)
    product_image: Optional[str]
    sku: str = Field(..., max_length=100)
    unit_of_measure: Literal['mtr', 'mm', 'ltr', 'ml', 'cm', 'mg', 'gm', 'unit', 'pack']
    lead_time: int = Field(..., ge=0, le=999)

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[Literal['finished', 'semi-finished', 'raw']] = None
    description: Optional[str] = None
    product_image: Optional[str] = None
    sku: Optional[str] = None
    unit_of_measure: Optional[Literal['mtr', 'mm', 'ltr', 'ml', 'cm', 'mg', 'gm', 'unit', 'pack']] = None
    lead_time: Optional[int] = None

    class Config:
        extra = "forbid"

class ProductResponse(ProductBase):
    product_id: int
    created_date: datetime
    updated_date: datetime

    class Config:
        from_attributes = True

class PaginatedProductResponse(BaseModel):
    total: int
    page: int
    page_size: int
    items: list[ProductResponse] 