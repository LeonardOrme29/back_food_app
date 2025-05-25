from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.user_schema import User, UserLogin, LoginResponse, RegisterResponse
from models.user_model import UserModel
from database import get_db

router = APIRouter()

def get_user(db: Session, email: str):
    return db.query(UserModel).filter(UserModel.email == email).first()

def create_user(db: Session, user: User):
    db_user = UserModel(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.post("/register", response_model=RegisterResponse)
def register(user: User, db: Session = Depends(get_db)):
    if get_user(db, user.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    create_user(db, user)
    return {"message": "User registered successfully", "email": user.email}

@router.post("/login", response_model=LoginResponse)
def login(user: UserLogin, db: Session = Depends(get_db)):
    stored_user = get_user(db, user.email)
    if not stored_user or stored_user.password != user.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {
        "firstname": stored_user.firstname,
        "lastname": stored_user.lastname,
        "email": stored_user.email
    }
