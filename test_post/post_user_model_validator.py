from pydantic import BaseModel

class CreateUser(BaseModel):
    name: str
    job: str
    id: int
    createdAt: str # Add date time format validator

class RegisterSuccesful(BaseModel):
    id: int
    token: str

class RegisterOrLoginUnsuccesful(BaseModel):
    error: str

class LoginSuccesful(BaseModel):
    token: str


