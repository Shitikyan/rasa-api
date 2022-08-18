from fastapi import FastAPI
from pydantic import BaseModel
import requests


class RasaRequest(BaseModel):
    sender: str
    message: str


class RasaResponse(BaseModel):
    recipient_id: str
    text: str


app = FastAPI()
rasaUrl = "http://rasa:5005/webhooks/rest/webhook"

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/api/")
async def api(request: RasaRequest):
    pass


def toRasa(request: RasaRequest):
    # requests.post(rasaUrl, )
    return [1, 2]


def parseUserQuestion(body: RasaRequest):
    isCorrect = True

    response, err = toRasa(body)

    if response.text == "":
        isCorrect = False

