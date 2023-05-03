from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..config import SessionLocal
from models.student import Student

router = APIRouter()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@router.post("/students/")
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    db_student = Student(name=student.name, age=student.age)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

@router.get("/students/{student_id}")
def read_student(student_id: int, db: Session = Depends(get_db)):
    db_student = db.query(Student).filter(Student.id == student_id).first()
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

@router.put("/students/{student_id}")
def update_student(student_id: int, student: StudentUpdate, db: Session = Depends(get_db)):
    db_student = db.query(Student).filter(Student.id == student_id).first()
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")
    for var, value in vars(student).items():
        setattr(db_student, var, value) if value else None
    db.commit()
    db.refresh(db_student)
    return db_student

@router.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    db_student = db.query(Student).filter(Student.id == student_id).first()
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")
    db.delete(db_student)
    db.commit()
    return {"message": "Student deleted"}
