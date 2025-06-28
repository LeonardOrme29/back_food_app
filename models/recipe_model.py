from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class RecipeModel(Base):
    __tablename__ = "recipe"
    id = Column(Integer, primary_key=True, index=True)
    dish_id = Column(Integer, ForeignKey("dishmodel.id"), nullable=False)
    ingredient_id = Column(Integer, ForeignKey("ingredient.id"), nullable=False)

    dishmodel = relationship("DishmodelModel")
    ingredient = relationship("IngredientModel")
