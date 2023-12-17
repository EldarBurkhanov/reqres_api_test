from pydantic import BaseModel, field_validator
from typing import List

class User(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str

    @field_validator("email")
    def email_validator(cls, value):
        if not "@" in value: # Simple check, i know that i can do it better :)
            raise ValueError("Uncorrect Email format")
        return value

class Support(BaseModel):
    url: str
    text: str


class ListUsers(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: List[User]
    support: Support


class SingleUser(BaseModel):
    data: User
    support: Support


