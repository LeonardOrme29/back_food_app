from pydantic import BaseModel
from typing import Optional

class Dish(BaseModel):
    name: str
    category: str
    url_image: Optional[str] = None

    class Config:
        orm_mode = True

class DishResponse(BaseModel):
    id: int
    name: str
    category: str
    url_image: str
