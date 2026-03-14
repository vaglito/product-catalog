from fastapi import FastAPI, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from core.database import Base, engine, get_db
from core import crud
from core.schemas import CreateProduct, UpdateProduct, ProductOut, ProductPage

app = FastAPI(
    title="Catalogo de productos",
    version="0.1.0",
)

Base.metadata.create_all(bind=engine)


@app.get("/products", response_model=ProductPage)
def get_products(
    db: Session = Depends(get_db),
    q: str | None = Query(None, description="Buscar por descripcion"),
    price_min: float | None = Query(None, ge=0, description="Precio minimo"),
    price_max: float | None = Query(None, ge=0, description="Precio maximo"),
    order_for: str = Query("id", description="Ordenar por"),
    order_by: str = Query("asc", description="Ordenar de forma"),
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0),
):
    total, items = crud.get_products(
        db=db,
        q=q,
        price_min=price_min,
        price_max=price_max,
        order_for=order_for,
        order_by=order_by,
        limit=limit,
        offset=offset,
    )
    return {"total": total, "limit": limit, "offset": offset, "items": items}


@app.get("/products/{product_id}", response_model=ProductOut)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = crud.get_product(db, product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
        )
    return product


@app.post("/products", response_model=ProductOut, status_code=status.HTTP_201_CREATED)
def create_product(data: CreateProduct, db: Session = Depends(get_db)):
    return crud.create_product(db, data)


@app.put("/products/{product_id}", response_model=ProductOut)
def update_product(product_id: int, data: UpdateProduct, db: Session = Depends(get_db)):
    product = crud.update_product(db, product_id, data)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
        )
    return product


@app.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = crud.delete_product(db, product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
        )
    return
