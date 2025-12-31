from .Base import base
from sqlalchemy import Column,Integer,String,Float

class Catrgory(base):
    __tablename__='Catrgory'
    id= Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String(30),nullable=False)

