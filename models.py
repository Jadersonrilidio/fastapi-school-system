from sqlalchemy import Column, String, Text, Integer, ForeignKey, DateTime, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    profile = relationship("Profile", back_populates='student', uselist=False, cascade="all, delete-orphan")
    enrollments = relationship('Enrollment', back_populates='student', cascade="all, delete-orphan")
    subjects = relationship("Subject", secondary="enrollments", viewonly=True, lazy="selectin")
    # created_at = Column(DateTime(timezone=True), server_default=func.now())

class Profile(Base):
    __tablename__ = 'profiles'
    id = Column(Integer, primary_key=True, index=True)
    age = Column(Integer)
    email = Column(String(255), unique=True)
    address = Column(String(255))
    student_id = Column(Integer, ForeignKey('students.id'), unique=True)
    student = relationship("Student", back_populates='profile')
    # created_at = Column(DateTime(timezone=True), server_default=func.now())

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

class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(7), nullable=False, unique=True)
    name = Column(String(255), nullable=False, unique=True)
    description = Column(Text)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=False)
    teacher = relationship('Teacher', back_populates='subjects')
    enrollments = relationship('Enrollment', back_populates='subject', cascade='all, delete-orphan', lazy="selectin")
    students = relationship("Student", secondary="enrollments", viewonly=True,lazy="selectin")
    # created_at = Column(DateTime(timezone=True), server_default=func.now())

class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    subjects = relationship('Subject', back_populates='teacher', lazy="selectin")
    # created_at = Column(DateTime(timezone=True), server_default=func.now())
