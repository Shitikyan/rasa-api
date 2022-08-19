from fastapi import APIRouter
from routes.rasa_app import router as rasa_router
from routes.user import router as user_router
from routes.login import router as login_router
from routes.chat import router as chat_router

router = APIRouter()

router.include_router(rasa_router, prefix="/rasa")
router.include_router(user_router, prefix="/user")
router.include_router(login_router, prefix="/login")
router.include_router(chat_router, prefix="/chat")
