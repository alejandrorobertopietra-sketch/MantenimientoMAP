from sqlalchemy import Column, Integer, String
from core.database import Base

class SparePart(Base):
    __tablename__ = "spare_parts"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    code = Column(String)
    stock = Column(Integer)
    min_stock = Column(Integer)