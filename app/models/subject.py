from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from config import Base

class Subject(Base):
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    student_id = Column(Integer, ForeignKey("students.id"))
    student = relationship("Student", back_populates="subjects")
