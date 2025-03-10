from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from . import models, schemas, database

router = APIRouter(prefix="/product", tags=["products"])

@router.get("/list", response_model=schemas.PaginatedProductResponse)
def list_products(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
    db: Session = Depends(database.get_db)
):
    skip = (page - 1) * page_size
    total = db.query(models.Product).count()
    products = db.query(models.Product).offset(skip).limit(page_size).all()
    
    return {
        "total": total,
        "page": page,
        "page_size": page_size,
        "items": products
    }

@router.get("/{pid}/info", response_model=schemas.ProductResponse)
def get_product(pid: int, db: Session = Depends(database.get_db)):
    product = db.query(models.Product).filter(models.Product.product_id == pid).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.post("/add", response_model=schemas.ProductResponse, status_code=201)
def create_product(product: schemas.ProductCreate, db: Session = Depends(database.get_db)):
    if db.query(models.Product).filter(models.Product.sku == product.sku).first():
        raise HTTPException(status_code=400, detail="SKU already exists")
    
    db_product = models.Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@router.put("/{pid}/update", response_model=schemas.ProductResponse)
def update_product(pid: int, product: schemas.ProductUpdate, db: Session = Depends(database.get_db)):
    db_product = db.query(models.Product).filter(models.Product.product_id == pid).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    if product.sku and product.sku != db_product.sku:
        if db.query(models.Product).filter(models.Product.sku == product.sku).first():
            raise HTTPException(status_code=400, detail="SKU already exists")
    
    update_data = product.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_product, key, value)
    
    db.commit()
    db.refresh(db_product)
    return db_product 