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


# ✅ READ all drugs (Synchronous Query)
@router.get("/", response_model=List[DrugResponse])
def get_drugs(db: Session = Depends(get_db)):  # Use `Session` instead of `AsyncSession`
    return db.query(Drug).all()  # Standard synchronous query


# ✅ CREATE a new drug (Synchronous Insert)
@router.post("/", response_model=DrugResponse)
def create_drug(drug: DrugCreate, db: Session = Depends(get_db)):  # Use `Session`
    existing_drug = db.query(Drug).filter(Drug.name == drug.name).first()

    if existing_drug:
        raise HTTPException(status_code=400, detail="Drug with this name already exists")

    db_drug = Drug(**drug.model_dump())  # Convert Pydantic model to dictionary
    db.add(db_drug)
    db.commit()  # ✅ No `await`, use standard commit
    db.refresh(db_drug)  # ✅ No `await`, use standard refresh

    return db_drug
