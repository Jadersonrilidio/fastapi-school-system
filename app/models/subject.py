from sqlalchemy import Column, String, Text, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


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
