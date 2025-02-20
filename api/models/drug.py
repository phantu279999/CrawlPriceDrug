from sqlalchemy import Column, Integer, String, DateTime, Index
from api.core.database import Base
import datetime

class Drug(Base):
    __tablename__ = "Drug"

    drug_id = Column(Integer, primary_key=True, autoincrement=True)
    declaration_date = Column(DateTime, nullable=True, default=datetime.datetime.utcnow)
    status = Column(String(255), nullable=True)
    petition = Column(String(255), nullable=True)
    name = Column(String(255), nullable=False, unique=True, index=True)
    hc_name = Column(String(255), nullable=True)
    nd_hl = Column(String(255), nullable=True)
    gplh_gpnk = Column(String(255), nullable=True)
    dosage_form = Column(String(255), nullable=True)
    packaging_specifications = Column(String(255), nullable=True)
    DVT = Column(String(50), nullable=True)
    price = Column(String(20), nullable=True)
    url = Column(String(200), nullable=True)

    # Define index explicitly
    __table_args__ = (Index("idx_drug_name", "name"),)
