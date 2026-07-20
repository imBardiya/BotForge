from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate
from app.core.database import get_db
from app.crud.user import create_user

router = APIRouter(
    prefix="/user",
    tags=["Users"],
)

@router.post("/")
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    
    return create_user(db, user)