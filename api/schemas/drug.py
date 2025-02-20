from datetime import datetime
from pydantic import BaseModel

class DrugBase(BaseModel):
    declaration_date: datetime | None = None
    status: str | None = None
    petition: str | None = None
    name: str
    hc_name: str | None = None
    nd_hl: str | None = None
    gplh_gpnk: str | None = None
    dosage_form: str | None = None
    packaging_specifications: str | None = None
    DVT: str | None = None
    price: str | None = None
    url: str | None = None

class DrugCreate(DrugBase):  # Schema for creating a new drug
    pass

class DrugUpdate(DrugBase):  # Schema for updating a drug
    pass

class DrugResponse(DrugBase):  # Schema for response
    drug_id: int

    class Config:
        from_attributes = True  # Required for SQLAlchemy integration
