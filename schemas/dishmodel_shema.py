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