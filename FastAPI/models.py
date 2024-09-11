#tables for sqlite application
from database import Base
from sqlalchemy import Column, Integer, String, Boolean, Float


#model
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String)
    email = Column(String)
    password = Column(String)