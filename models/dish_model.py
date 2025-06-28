from sqlalchemy import Column, Integer, String,ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class DishModel(Base):
    __tablename__ = "dish"
    id = Column(Integer, primary_key=True, index=True)
    category = Column(String, nullable=False)
    url_image = Column(String)
    create_at = Column(String)
    dishmodel_id= Column(Integer)
    user_id= Column(Integer,ForeignKey("dishmodel.id"))
    accuracy= Column(String)

    dishmodel = relationship("DishmodelModel")

