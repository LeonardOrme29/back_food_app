from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.dish_model import DishModel
from schemas.dish_schema import Dish,DishResponse
from database import get_db

router = APIRouter()

@router.get("/dishes", response_model=list[DishResponse])
def get_dishes(db: Session = Depends(get_db)):
    return db.query(DishModel).all()


@router.post("/dishes/upload", response_model=DishResponse)
def upload_dish(dish: Dish, db: Session = Depends(get_db)):
    new_dish = DishModel(
        name=dish.name,
        category=dish.category,
        url_image=dish.url_image
    )
    db.add(new_dish)
    db.commit()
    db.refresh(new_dish)
    return new_dish