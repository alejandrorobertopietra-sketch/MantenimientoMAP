from sqlalchemy import Column, Integer, String
from core.database import Base

class Equipment(Base):
    __tablename__ = "equipment"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    code = Column(String)
    area = Column(String)
    brand = Column(String)
    model = Column(String)