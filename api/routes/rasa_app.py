from fastapi import APIRouter

from rasa.app import parse_user_question
from rasa.models import RasaResponse, RasaRequest


router = APIRouter()


@router.post("/parse_user_question/")
async def api(request: RasaRequest):
    response: RasaResponse = parse_user_question(request)
    return response
