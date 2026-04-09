from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from core.database import SessionLocal, engine
from core.database import Base

from models.equipment import Equipment
from models.workorder import WorkOrder
from models.spareparts import SparePart

app = FastAPI(title="Mantenimiento AP PRO")

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"Sistema": "Mantenimiento AP PRO funcionando"}

@app.post("/equipment")
def create_equipment(
    name: str,
    code: str,
    area: str,
    brand: str,
    model: str,
    db: Session = Depends(get_db)
):
    equipment = Equipment(
        name=name,
        code=code,
        area=area,
        brand=brand,
        model=model
    )

    db.add(equipment)
    db.commit()
    db.refresh(equipment)

    return equipment

@app.get("/equipment")
def list_equipment(db: Session = Depends(get_db)):
    return db.query(Equipment).all()

@app.post("/workorder")
def create_workorder(
    equipment_id: int,
    technician: str,
    description: str,
    status: str,
    db: Session = Depends(get_db)
):
    order = WorkOrder(
        equipment_id=equipment_id,
        technician=technician,
        description=description,
        status=status
    )

    db.add(order)
    db.commit()

    return order

@app.get("/workorders")
def list_orders(db: Session = Depends(get_db)):
    return db.query(WorkOrder).all()

@app.post("/sparepart")
def create_sparepart(
    name: str,
    code: str,
    stock: int,
    min_stock: int,
    db: Session = Depends(get_db)
):
    part = SparePart(
        name=name,
        code=code,
        stock=stock,
        min_stock=min_stock
    )

    db.add(part)
    db.commit()

    return part

@app.get("/spareparts")
def list_spareparts(db: Session = Depends(get_db)):
    return db.query(SparePart).all()