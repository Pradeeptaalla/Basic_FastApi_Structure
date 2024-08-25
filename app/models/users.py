# app/models/users.py
from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(500), nullable=True)
    password = Column(String(500), nullable=True)
    
   
