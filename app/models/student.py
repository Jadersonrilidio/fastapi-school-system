from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from app.database import Base


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    profile = relationship("Profile", back_populates='student', uselist=False, cascade="all, delete-orphan")
    enrollments = relationship('Enrollment', back_populates='student', cascade="all, delete-orphan")
    subjects = relationship("Subject", secondary="enrollments", viewonly=True, lazy="selectin")
    # created_at = Column(DateTime(timezone=True), server_default=func.now())
