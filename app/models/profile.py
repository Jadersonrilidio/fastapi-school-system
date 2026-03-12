from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Profile(Base):
    __tablename__ = 'profiles'
    id = Column(Integer, primary_key=True, index=True)
    age = Column(Integer)
    email = Column(String(255), unique=True)
    address = Column(String(255))
    student_id = Column(Integer, ForeignKey('students.id'), unique=True)
    student = relationship("Student", back_populates='profile')
    # created_at = Column(DateTime(timezone=True), server_default=func.now())
