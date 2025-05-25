from sqlalchemy import Column, Integer, String
from database import Base

class DishModel(Base):
    __tablename__ = "dish"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    url_image = Column(String)
