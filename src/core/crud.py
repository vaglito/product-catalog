from typing import Optional, Tuple, List
from sqlalchemy.orm import Session
from sqlalchemy import func
from .models import Product
from .schemas import CreateProduct, UpdateProduct

_ORDERABLE_FIELDS = {
    "id": Product.id,
    "description": Product.description,
    "price": Product.price,
}


def get_products(
    db: Session,
    q: Optional[str] = None,
    price_min: Optional[float] = None,
    price_max: Optional[float] = None,
    order_for: str = "id",
    order_by: str = "asc",
    limit: int = 10,
    offset: int = 0,
) -> Tuple[int, List[Product]]:

    query = db.query(Product)
    if q:
        query = query.filter(Product.description.ilike(f"%{q}%"))

    if price_min is not None:
        query = query.filter(Product.price >= price_min)

    if price_max is not None:
        query = query.filter(Product.price <= price_max)

    total = query.with_entities(func.count()).scalar() or 0

    col = _ORDERABLE_FIELDS.get(order_for, Product.id)
    col = col.desc() if order_by.lower() == "desc" else col.asc()

    items = query.order_by(col).offset(offset).limit(limit).all()

    return total, items


def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()


def create_product(db: Session, product: CreateProduct):
    product = Product(**product.model_dump())
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


def update_product(db: Session, product_id: int, product: UpdateProduct):
    db_product = get_product(db, product_id)
    if db_product:
        db_product.description = product.description
        db_product.price = product.price
        db.commit()
        db.refresh(db_product)
    return db_product


def delete_product(db: Session, product_id: int):
    product = get_product(db, product_id)
    if product:
        db.delete(product)
        db.commit()
    return product
