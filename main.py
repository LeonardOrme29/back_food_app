from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine
from models import user_model, dish_model, ingredient_model, recipe_model
from routers import auth, dish, ingredient,dishmodel
from iaModel import predict

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(auth.router, tags=["Auth"])
app.include_router(dish.router, tags=["Dishes"])
app.include_router(ingredient.router, tags=["Ingredients"])
app.include_router(predict.router, tags=["Predicts"])
app.include_router(dishmodel.router, tags=["dishmodel"])

@app.get("/")
def root():
    return {"mensaje": "¡Hola desde FastAPI modularizado!"}
