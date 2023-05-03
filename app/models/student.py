from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from config import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    subjects = relationship("Subject", back_populates="student")
