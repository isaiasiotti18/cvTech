from pydantic import BaseModel

class Education(BaseModel):
    degree: str
    institution: str
    description: str