from typing import TYPE_CHECKING
from pydantic import BaseModel, ConfigDict, Field
from app.schemas.profile_schema import ProfileCreate, ProfileUpdate, ProfileSummary

if TYPE_CHECKING:
    from app.schemas.subject_schema import SubjectSummary


class StudentBase(BaseModel):
    name: str

class StudentCreate(StudentBase):
    profile: ProfileCreate | None = None

class StudentUpdate(BaseModel):
    name: str | None = None
    profile: ProfileUpdate | None = None

class StudentSummary(StudentBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class StudentDetail(StudentBase):
    id: int
    profile: ProfileSummary | None = None
    subjects: list["SubjectSummary"] = Field(default_factory=list)
    model_config = ConfigDict(from_attributes=True)
