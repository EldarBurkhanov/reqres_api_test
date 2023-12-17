from pydantic import BaseModel


# Could be used with Patch
class UpdateUser(BaseModel):
    name: str
    job: str
    updatedAt: str # Add date validator



