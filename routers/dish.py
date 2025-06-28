from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.dish_model import DishModel
from models.dishmodel_model import DishmodelModel
from schemas.dish_schema import DishCreate,DishResponse
from database import get_db
from datetime import datetime, timezone

router = APIRouter()

@router.get("/dishes", response_model=list[DishResponse])
def get_dishes(db: Session = Depends(get_db)):
    return db.query(DishModel).all()


@router.post("/dishes/upload", response_model=DishResponse)
def upload_dish(dish: DishCreate, db: Session = Depends(get_db)):

    dish_model_entry = db.query(DishmodelModel).filter(
        DishmodelModel.label == dish.category,
    ).first()
    if not dish_model_entry:
        raise HTTPException(status_code=404, detail="Dishmodel not found for the given category and label")
    
    current_time_aware_utc = datetime.now(timezone.utc)
    current_time_str = current_time_aware_utc.isoformat()

    new_dish = DishModel(
        category=dish.category,
        url_image=dish.url_image,
        create_at=current_time_str,
        dishmodel_id=dish_model_entry.id,
        user_id=dish.user_id,
        accuracy=dish.accuracy
    )
    db.add(new_dish)
    db.commit()
    db.refresh(new_dish)
    return new_dish 

@router.get("/dishmodels")
def get_dishmodels(db: Session = Depends(get_db)):
    return db.query(DishmodelModel).all()