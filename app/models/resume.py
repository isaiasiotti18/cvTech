from pydantic import BaseModel
from typing import List

from app.models.experience import Experience
from app.models.education import Education

class Resume(BaseModel):
    name: str
    contact: str
    experience: List[Experience]
    education: List[Education]