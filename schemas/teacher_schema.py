from typing import TYPE_CHECKING
from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from schemas.subject_schema import SubjectSummary


class TeacherBase(BaseModel):
    name: str

class TeacherCreate(TeacherBase):
    pass

class TeacherUpdate(BaseModel):
    name: str | None = None

class TeacherSummary(TeacherBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class TeacherDetail(TeacherBase):
    id: int
    subjects: list["SubjectSummary"] = Field(default_factory=list)
    model_config = ConfigDict(from_attributes=True)
