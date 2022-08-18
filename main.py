import json

from fastapi import FastAPI
from pydantic import BaseModel
import requests


class RasaRequest(BaseModel):
    sender: str
    message: str


class RasaResponse(BaseModel):
    recipient_id: str
    text: str
    is_correct: bool


app = FastAPI()
rasaUrl = "http://rasa:5005/webhooks/rest/webhook"


@app.post("/api/")
async def api(request: RasaRequest):
    response = parse_user_question(request)
    return response


def to_rasa(request: RasaRequest):
    r = requests.post(rasaUrl, data=request.json())
    res_obj = json.loads(r.text)
    response: RasaResponse = RasaResponse(recipient_id=res_obj['recipient_id'], text=res_obj['text'], is_correct=res_obj['correct'])

    return response


def parse_user_question(body: RasaRequest):
    response = to_rasa(body)

    return response
