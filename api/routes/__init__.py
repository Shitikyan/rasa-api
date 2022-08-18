from fastapi import APIRouter
from api.routes.rasa_app import router as rasa_router

router = APIRouter()

router.include_router(rasa_router, prefix="/rasa", tags=["mobile"])
