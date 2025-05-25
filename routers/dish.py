from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.dish_model import DishModel
from schemas.dish_schema import Dish
from database import get_db

router = APIRouter()

@router.get("/dishes", response_model=list[Dish])
def get_dishes(db: Session = Depends(get_db)):
    return db.query(DishModel).all()
