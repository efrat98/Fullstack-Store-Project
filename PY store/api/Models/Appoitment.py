# Models/Appointment.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from Models.Base import base
from sqlalchemy.orm import relationship


class Appointment(base):
    __tablename__ = 'appointments'
    id = Column(Integer, primary_key=True)

    # פרטי הלקוח
    client_name = Column(String(100), nullable=False)
    client_phone = Column(String(20))
    client_email = Column(String(100))

    # פרטי התור
    service_id = Column(Integer, ForeignKey('services.id'))
    service = relationship("Service")

    start_time = Column(DateTime, nullable=False)  # תאריך ושעת התחלה
    end_time = Column(DateTime, nullable=False)  # תאריך ושעת סיום (מחושב ע"פ משך השירות)

    is_confirmed = Column(Boolean, default=False)

    def __repr__(self):
        return f"<Appointment(service={self.service_id}, start={self.start_time})>"