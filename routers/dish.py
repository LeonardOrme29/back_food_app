from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from models.dish_model import DishModel
from models.dishmodel_model import DishmodelModel
from schemas.dishmodel_shema import DishAverageResponse,UserIDRequest
from schemas.dish_schema import DishCreate,DishResponse
from database import get_db
from datetime import datetime, timezone
from sqlalchemy import func

router = APIRouter()

@router.get("/dishes", response_model=list[DishResponse])
def get_dishes(user_id: int | None = None, db: Session = Depends(get_db)):
    query = db.query(DishModel)
    if user_id is not None:
        query = query.filter(DishModel.user_id == user_id)
    return query.all()



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


@router.post("/dishes/average", response_model=DishAverageResponse)
def get_dish_averages_by_user_id(
    request: UserIDRequest,
    db: Session = Depends(get_db)
):
    avg = (
        db.query(
            func.avg(DishmodelModel.grasas).label("average_grasas"),
            func.avg(DishmodelModel.carbohidratos).label("average_carbohidratos"),
            func.avg(DishmodelModel.proteinas).label("average_proteinas"),
        )
        .join(DishModel, DishmodelModel.id == DishModel.dishmodel_id)  # JOIN explícito
        .filter(DishModel.user_id == request.user_id)
        .one()
    )

    return {
        "average_grasas": avg.average_grasas or 0,
        "average_carbohidratos": avg.average_carbohidratos or 0,
        "average_proteinas": avg.average_proteinas or 0
    }
