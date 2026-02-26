from sqlalchemy import Column, Integer, String, Date, Time
from app.models.base import Base

class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True)
    roll_no = Column(String(20))
    subject = Column(String(50))
    date = Column(Date)
    time = Column(Time)
    status = Column(String(10))
    