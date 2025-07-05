from pydantic import BaseModel
from typing import Optional


class DishmodelResponse(BaseModel):
    id: int
    name: str
    label: str
    category: str
    grasas: float
    carbohidrato: float
    proteinas: float

class DishAverageResponse(BaseModel):
    average_grasas: float
    average_carbohidratos: float
    average_proteinas: float

class UserIDRequest(BaseModel):
    user_id: int