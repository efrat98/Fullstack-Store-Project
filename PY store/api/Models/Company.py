from .Base import base
from sqlalchemy import Column,Integer,String,Float


class Company(base):
    __tablename__ = 'Company'  # לאיזה טבלה אני שייכת
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(60), nullable=False)