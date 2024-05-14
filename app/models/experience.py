from pydantic import BaseModel

class Experience(BaseModel):
  title: str
  company: str
  description: str