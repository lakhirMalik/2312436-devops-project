import os
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import get_db, engine, check_db_connection
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

STUDENT_REG_NO = os.getenv("STUDENT_REG_NO", "2312436")


class StudentCreate(BaseModel):
    name: str
    reg_no: str
    email: str = None


@app.get("/health")
def health():
    db_status = "connected" if check_db_connection() else "disconnected"
    return {
        "status": "ok",
        "db": db_status,
        "student": STUDENT_REG_NO
    }


@app.post("/students", status_code=201)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    existing = db.query(models.Student).filter(
        models.Student.reg_no == student.reg_no
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail="reg_no already exists")
    new_student = models.Student(
        name=student.name,
        reg_no=student.reg_no,
        email=student.email
    )
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student


@app.get("/students")
def get_students(db: Session = Depends(get_db)):
    return db.query(models.Student).all()


@app.get("/students/{reg_no}")
def get_student(reg_no: str, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(
        models.Student.reg_no == reg_no
    ).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student
