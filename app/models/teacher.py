from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from app.database import Base


class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    subjects = relationship('Subject', back_populates='teacher', lazy="selectin")
    # created_at = Column(DateTime(timezone=True), server_default=func.now())
