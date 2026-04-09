from sqlalchemy import Column, Integer, String, ForeignKey
from core.database import Base

class WorkOrder(Base):
    __tablename__ = "work_orders"

    id = Column(Integer, primary_key=True)
    equipment_id = Column(Integer, ForeignKey("equipment.id"))
    technician = Column(String)
    description = Column(String)
    status = Column(String)