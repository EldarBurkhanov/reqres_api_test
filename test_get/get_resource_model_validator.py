from pydantic import BaseModel, field_validator
from typing import List
import re

class Resource(BaseModel):
    id: int
    name: str
    year: int
    color: str
    pantone_value: str


    @field_validator("color")
    def validate_color(cls, value):
        if not value[0] == "#" and len(value) == 7:
            raise ValueError(f"Invalid Color Format, Color Should be in HEX format, your format: {value}")
        return value

    @field_validator("pantone_value")
    def pantone_value(cls, value):
        if not re.match(r"^\d{2}-\d{4}$", value):
            raise ValueError(f"Invalid Pantone value format, Pantone value should be `17-2031` format, your format: {value}")
        return value

class Support(BaseModel):
    # Could be replaced by importing from GUMV
    url: str
    text: str

class ListResourcees(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: List[Resource]
    support: Support


class SingleResource(BaseModel):
    data: Resource
    support: Support






