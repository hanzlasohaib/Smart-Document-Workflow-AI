from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional

# Data sent when registering
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str


# Data returned to client
class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: str

    model_config = ConfigDict(from_attributes=True)

class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
