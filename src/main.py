from fastapi import FastAPI
from core.database import Base, engine
from router import products

app = FastAPI(
    title="Catalogo de productos",
    version="0.2.0",
)

Base.metadata.create_all(bind=engine)

app.include_router(products.router)
