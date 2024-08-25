# app/routers/v1/users.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.users import Users
from app.schemas.users import UsersCreate, UsersResponse

router = APIRouter()

@router.post("/users", response_model=UsersResponse)
def create_users(
    users: UsersCreate, db: Session = Depends(get_db)
):
    db_users = Users(**users.dict())
    db.add(db_users)
    db.commit()
    db.refresh(db_users)
    return db_users

@router.get("/users", response_model=list[UsersResponse])
def get_users(db: Session = Depends(get_db)):
    return db.query(Users).all()
