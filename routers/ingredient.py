from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.recipe_model import RecipeModel
from models.ingredient_model import IngredientModel
from schemas.ingredient_schema import IngredientWithQuantity
from database import get_db

router = APIRouter()

@router.get("/dishes/{dish_id}/ingredients", response_model=list[IngredientWithQuantity])
def get_ingredients_for_dish(dish_id: int, db: Session = Depends(get_db)):
    results = (
        db.query(RecipeModel, IngredientModel)
        .join(IngredientModel, RecipeModel.ingredient_id == IngredientModel.id)
        .filter(RecipeModel.dish_id == dish_id)
        .all()
    )
    return [IngredientWithQuantity(name=i.name, category=i.category) for _, i in results]
