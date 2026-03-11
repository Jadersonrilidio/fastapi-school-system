from pydantic import BaseModel, EmailStr, ConfigDict


class ProfileBase(BaseModel):
    age: int | None = None
    email: EmailStr | None = None
    address: str | None = None

class ProfileCreate(ProfileBase):
    pass

class ProfileUpdate(ProfileBase):
    pass

class ProfileSummary(ProfileBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
