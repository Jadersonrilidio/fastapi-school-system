from sqlalchemy import Column, Integer, ForeignKey, DateTime, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base


class Enrollment(Base):
    __tablename__ = 'enrollments'
    __table_args__ = (
        UniqueConstraint('student_id', 'subject_id', name='unique_student_subject'),
    )
    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime(timezone=True), server_default=func.now())
    student_id = Column(Integer, ForeignKey('students.id'))
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    student = relationship("Student", back_populates='enrollments')
    subject = relationship("Subject", back_populates='enrollments')
    # created_at = Column(DateTime(timezone=True), server_default=func.now())
