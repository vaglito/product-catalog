from pydantic import BaseModel, Field


class ProductBase(BaseModel):
    description: str = Field(min_length=5, max_length=100)
    price: float = Field(gt=0)


class CreateProduct(ProductBase):
    pass


class UpdateProduct(ProductBase):
    description: str = Field(min_length=5, max_length=100)
    price: float = Field(gt=0)


class ProductOut(ProductBase):
    id: int

    class Config:
        form_attributes = True


class ProductPage(BaseModel):
    total: int
    limit: int
    offset: int
    items: list[ProductOut]
