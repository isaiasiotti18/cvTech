from fastapi import APIRouter
from app.api.routes.resume import router as resumeRouter

router = APIRouter()
router.include_router(resumeRouter, prefix="/resume", tags=["resume"])