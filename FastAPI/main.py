from fastapi import FastAPI, HTTPException, Depends
from typing import Annotated
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import SessionLocal, engine
import models
# A way to defend from cross origin requests, something outside the application calling it
# as the React application is going to be different from the fastAPI, we need to enable it 
# somehow
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Now another application can call the api, but only if it running
# on localhost:3000
origins = [
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins
)

#pydantic
class UserBase(BaseModel):
    name: str
    email: str
    password: str

class UserModel(UserBase)
    id: int

    class Config:
        orm_mode = True

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()

#dependency injection
db_dependency = Annotated[Session, Depends(get_db)]
# Creating the database and the columns automatically when the fastAPI
# is created
models.Base.metadata.create_all(bind = engine)

# Creating th endpoints for the application
@add.post('/users/', respond_model = UserModel)