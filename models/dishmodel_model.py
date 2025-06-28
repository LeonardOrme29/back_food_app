from sqlalchemy import Column, Integer, String, Float
from database import Base

class DishmodelModel(Base):
    __tablename__ = "dishmodel"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)        
    label = Column(String, unique=True, index=True) # Od
    category = Column(String)    
    grasas = Column(Float)      
    carbohidratos = Column(Float)
    proteinas = Column(Float)