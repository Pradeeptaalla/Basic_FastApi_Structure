from pydantic import BaseModel

class UsersCreate(BaseModel):
    name: str
    password: str
    

class UsersResponse(BaseModel):
    id: int
    name: str
    password: str
   

    class Config:
        orm_mode = True
