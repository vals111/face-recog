from sqlalchemy import Column, Integer, String, Boolean
from app.models.base import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    roll_no = Column(String(20), unique=True)
    name = Column(String(100))
    email = Column(String(100))
    password = Column(String(255))
    branch = Column(String(50))
    section = Column(String(10))
    active = Column(Boolean, default=True)
