from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.core.config import settings

from typing import Generator


engine = create_engine(
    settings.database_url,
    echo=settings.debug,   
)

SessionLocal = sessionmaker(     
    bind=engine,
    autoflush=False,
    autocommit=False
)

class Base(DeclarativeBase):
    pass

def get_db() -> Generator:
    db = SessionLocal()   # این خط هربار اجرا بشه یک سیزن جدید ساخته میشه

    try:
        yield db
    finally:
        db.close()
