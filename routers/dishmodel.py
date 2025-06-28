from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.dishmodel_model import DishmodelModel
from schemas.dishmodel_shema import DishmodelResponse
from database import get_db

router = APIRouter()

@router.get("/dishes2")
def get_dishes(db: Session = Depends(get_db)):
    return db.query(DishmodelModel).all()


@router.get("/dishes/{dish_id}")
def get_dish_by_id(dish_id: int, db: Session = Depends(get_db)):
    dish = db.query(DishmodelModel).filter(DishmodelModel.id == dish_id).first()
    if dish is None:
        raise HTTPException(status_code=404, detail="Dish not found")
    return dish