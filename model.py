from pydantic import BaseModel
from typing import Optional

class Todo(BaseModel):
    title: str
    description:str

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None

class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None

class User(BaseModel):
    username = str
    password = str
    