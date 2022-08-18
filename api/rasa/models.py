from pydantic import BaseModel


class RasaRequest(BaseModel):
    sender: str
    message: str


class RasaResponse(BaseModel):
    recipient_id: str
    text: str
    is_correct: bool