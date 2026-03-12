from sqlalchemy.orm import Session
from app.models import Student
from typing import List

class StudentRepository:

    @staticmethod
    def list(db: Session) -> List[Student]:
        return db.query(Student).all()

    @staticmethod
    def get(db: Session, student_id: int) -> Student:
        return db.get(Student, student_id)

    @staticmethod
    def create(db: Session, student: Student) -> Student:
        db.add(student)
        db.commit()
        db.refresh(student)
        return student

    @staticmethod
    def update(db: Session, student: Student) -> Student:
        db.commit()
        db.refresh(student)
        return student

    @staticmethod
    def delete(db: Session, student: Student) -> None:
        db.delete(student)
        db.commit()
