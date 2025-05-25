from sqlalchemy import Column, Integer, String
from database import Base

class IngredientModel(Base):
    __tablename__ = "ingredient"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
