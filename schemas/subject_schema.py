from typing import TYPE_CHECKING
from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from schemas.teacher_schema import TeacherSummary
    from schemas.student_schema import StudentSummary


class SubjectBase(BaseModel):
    code: str
    name: str
    description: str | None = None

class SubjectCreate(SubjectBase):
    teacher_id: int

class SubjectUpdate(BaseModel):
    code: str | None = None
    name: str | None = None
    description: str | None = None
    teacher_id: int | None = None

class SubjectSummary(SubjectBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class SubjectDetail(SubjectBase):
    id: int
    teacher: "TeacherSummary"
    students: list["StudentSummary"] = Field(default_factory=list)
    model_config = ConfigDict(from_attributes=True)
