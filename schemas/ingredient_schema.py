from pydantic import BaseModel

class IngredientWithQuantity(BaseModel):
    name: str
    category: str

    class Config:
        orm_mode = True
