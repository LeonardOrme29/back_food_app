from pydantic import BaseModel
from typing import Optional
from pydantic import BaseModel

class Dish(BaseModel):
    category: str
    url_image: Optional[str] = None
    create_at: str
    dishmodel_id: int
    user_id: int
    accuracy: str
    

    class Config:
        orm_mode = True

class DishResponse(BaseModel):
    id: int
    category: str
    url_image: str
    create_at: str
    dishmodel_id: int
    user_id: int
    accuracy: str

class DishCreate(BaseModel):
    category: str
    url_image: str 
    user_id: int
    accuracy: str