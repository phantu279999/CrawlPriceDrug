import os
import sys
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from api.core.config import DATABASE_URL

# Create engine
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

try:
    db = SessionLocal()
    db.execute(text("SELECT 1"))  # ✅ Use `text()` for raw SQL
    print("✅ Connection successful!")
    db.close()
except Exception as e:
    print("❌ Connection failed:", str(e))
