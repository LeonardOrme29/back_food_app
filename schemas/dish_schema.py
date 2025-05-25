from pydantic import BaseModel
from typing import Optional

class Dish(BaseModel):
    id: int
    name: str
    category: str
    url_image: Optional[str] = None

    class Config:
        orm_mode = True
