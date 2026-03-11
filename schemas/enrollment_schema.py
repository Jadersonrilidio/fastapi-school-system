from datetime import datetime
from typing import TYPE_CHECKING
from pydantic import BaseModel, ConfigDict

if TYPE_CHECKING:
    from schemas.student_schema import StudentSummary
    from schemas.subject_schema import SubjectSummary


class EnrollmentBase(BaseModel):
    pass

class EnrollmentCreate(EnrollmentBase):
    student_id: int
    subject_id: int

class EnrollmentSummary(EnrollmentBase):
    id: int
    date: datetime
    student_id: int
    subject_id: int
    model_config = ConfigDict(from_attributes=True)

class EnrollmentDetail(EnrollmentBase):
    id: int
    date: datetime
    student: "StudentSummary"
    subject: "SubjectSummary"
    model_config = ConfigDict(from_attributes=True)
