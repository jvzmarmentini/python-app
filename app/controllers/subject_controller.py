from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from config import SessionLocal
from models.subject import Subject

router = APIRouter()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@router.post("/students/{student_id}/subjects/")
def create_subject_for_student(student_id: int, subject: SubjectCreate, db: Session = Depends(get_db)):
    db_subject = Subject(name=subject.name, student_id=student_id)
    db.add(db_subject)
    db.commit()
    db.refresh(db_subject)
    return db_subject

@router.get("/students/{student_id}/subjects/")
def read_subjects_for_student(student_id: int, db: Session = Depends(get_db)):
    db_subjects = db.query(Subject).filter(Subject.student_id == student_id).all()
    return db_subjects

@router.get("/subjects/{subject_id}")
def read_subject(subject_id: int, db: Session = Depends(get_db)):
    db_subject = db.query(Subject).filter(Subject.id == subject_id).first()
    if not db_subject:
        raise HTTPException(status_code=404, detail="Subject not found")
    return db_subject

@router.put("/subjects/{subject_id}")
def update_subject(subject_id: int, subject: SubjectUpdate, db: Session = Depends(get_db)):
    db_subject = db.query(Subject).filter(Subject.id == subject_id).first()
    if not db_subject:
        raise HTTPException(status_code=404, detail="Subject not found")
    for var, value in vars(subject).items():
        setattr(db_subject, var, value) if value else None
    db.commit()
    db.refresh(db_subject)
    return db_subject

@router.delete("/subjects/{subject_id}")
def delete_subject(subject_id: int, db: Session = Depends(get_db)):
    db_subject = db.query(Subject).filter(Subject.id == subject_id).first()
    if not db_subject:
        raise HTTPException(status_code=404, detail="Subject not found")
    db.delete(db_subject)
    db.commit()
    return {"message": "Subject deleted"}
