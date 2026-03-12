from typing import List
from sqlalchemy.orm import Session
from app.repositories import StudentRepository
from app.models import Student, Profile
from app.schemas import StudentCreate


class StudentService:

    @staticmethod
    def list_students(db: Session) -> List[Student]:
        return StudentRepository.list(db)
    
    @staticmethod
    def get_student(student_id: int, db: Session) -> Student | None:
        student = StudentRepository.get(db, student_id)
        return student if student else None
    
    @staticmethod
    def create_student(student_data: StudentCreate, db: Session) -> Student:
        student = Student(name=student_data.name)
        if student_data.profile:
            profile = Profile(**student_data.profile.model_dump())
            setattr(student, 'profile', profile)
        return StudentRepository.create(db, student)

    @staticmethod
    def delete_student(student_id: int, db: Session) -> bool:
        student = StudentRepository.get(db, student_id)
        if not student:
            return False
        StudentRepository.delete(db, student)
        return True
