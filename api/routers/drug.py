import os
import sys
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from api.core.database import get_db
from api.models.drug import Drug
from api.schemas.drug import DrugCreate, DrugResponse

router = APIRouter()


@router.get("/", response_model=List[DrugResponse])
def get_drugs(db: Session = Depends(get_db)):
    return db.query(Drug).all()


@router.post("/", response_model=DrugResponse)
def create_drug(drug: DrugCreate, db: Session = Depends(get_db)):
    existing_drug = db.query(Drug).filter(Drug.name == drug.name).first()

    if existing_drug:
        raise HTTPException(status_code=400, detail="Drug with this name already exists")

    db_drug = Drug(**drug.model_dump())
    db.add(db_drug)
    db.commit()
    db.refresh(db_drug)

    return db_drug
