# Models/Schedule.py
from sqlalchemy import Column, Integer, Time, String, ForeignKey
from Models.Base import base
from sqlalchemy.orm import relationship

class Schedule(base):
    __tablename__ = 'schedule'
    id = Column(Integer, primary_key=True)
    day_of_week = Column(Integer, nullable=False) # 0=שני, 6=ראשון, או שימוש במספרים מקובלים (0-6)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    # ניתן לשייך לנותן שירות ספציפי אם יש מספר עובדים
    # provider_id = Column(Integer, ForeignKey('users.id'))
    # provider = relationship("User")

    def __repr__(self):
        return f"<Schedule(day={self.day_of_week}, start={self.start_time}, end={self.end_time})>"