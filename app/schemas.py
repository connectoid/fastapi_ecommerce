from decimal import Decimal

from pydantic import BaseModel, Field, ConfigDict

class CategoryCreate(BaseModel):
    """
    Модель для создания и обновления категории.
    Испо
    name: str = Field(..., min_length=3, max_length=50,
                      description='Name of category (3-50 symbols)')
    parent_id: int | None = Field(None, description='ID of parent category, if exists')


class Category(BaseModel):
    """
    Модель для ответа с данными категории.
    Используется в GET-запросах.
    """
    id: int = Field(..., description='Unique ID of category')
    name: str = Field(..., description='Name of category')
    parent_id: int | None = Field(None, description='ID of parent category, if exists')
    is_active: bool = Field(..., description='Is category active')

    model_config: ConfigDict(from_attributes=True)


class ProductCreate(BaseModel):
    """
    Модель для создания и обновления товара.
    Используется в POST и PUT запросах.
    """
    name: str = Field(..., min_length=3, max_length=100,
                      description='Name of product (3-100 symbols)')
    description: str | None = Field(None, max_length=500,
                        description='Description of product (max 500 symbols)')
    price: Decimal = Field(..., gt=0, description='Price of product', decimal_places=2)
    image: str | None = Field(None, max_length=200, description='URL of image')
    stock: int = Field(..., ge=0, description='Amount of products in stock')
    category_id: int = Field(..., description='ID of product category')


class Product(BaseModel):
    """
    Модель для ответа с данными товара.
    Используется в GET-запросах.
    """
    id: int = Field(..., description="Уникальный идентификатор товара")
    name: str = Field(..., description="Название товара")
    description: str | None = Field(None, description="Описание товара")
    price: Decimal = Field(..., description="Цена товара в рублях", gt=0, decimal_places=2)
    image_url: str | None = Field(None, description="URL изображения товара")
    stock: int = Field(..., description="Количество товара на складе")
    category_id: int = Field(..., description="ID категории")
    is_active: bool = Field(..., description="Активность товара")

    model_config = ConfigDict(from_attributes=True)