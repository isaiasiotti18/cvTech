from fastapi import APIRouter, HTTPException
from app.models.resume import Resume
from app.services.resumeService import createResume

router = APIRouter()

@router.post(path="/generate_resume", response_model=dict)
def generateResume(resume: Resume):
  try:
    file_path = createResume(resume)
    return {"message": "Currículo criado com sucesso!", "file_path": file_path}
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
  
@router.get(path="/list_resume")
def getResume():
  return {"Hello": "World"}