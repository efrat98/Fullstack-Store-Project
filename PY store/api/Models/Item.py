
from sqlalchemy import Column,Integer,String,Float,ForeignKey# מייבאים מספריית אס קיו אל אלכמי את המשתנים שמאפשרים לנו להגדיר את מבנה העמודות בטבלה
from .Company import Company#
from .Category import Catrgory
from .Base import base
from sqlalchemy.orm import relationship

class Item(base):

    __tablename__ = 'Item'  # לאיזה טבלה אני שייכת
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(60), nullable=False, )
    price = Column(Float, nullable=False)
    count = Column(Integer, nullable=False, default=0)
    img= Column(Integer, nullable=False)
    category_id=Column(Integer,ForeignKey(Catrgory.id))
    company_id=Column(Integer,ForeignKey(Company.id))# שדה שמהווה מפתח זר של שדה איי די מטבלת קומפני
    category = relationship("Catrgory", backref="items")
    company = relationship("Company", backref="items")

    def to_dict(self):
        company_name = self.company.name if self.company else None
        category_name = self.category.name if self.category else None

        return {

            'id': self.id,
            'name': self.name,
            'price': self.price,
            'count': self.count,
            'img': self.img,
            'category_id': self.category_id,
            'company_id': self.company_id,
            'company_name': company_name,
            'category_name': category_name

        }