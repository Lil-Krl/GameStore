from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class UserPatch(BaseModel):
    username: str | None = None
    email: EmailStr | None = None

class UserOut(UserBase):
    id: int

    class Config:
        from_attributes = True
