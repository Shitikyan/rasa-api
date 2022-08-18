from api.rasa.models import RasaRequest, RasaResponse
import requests
import json
import config

rasaUrl = config.RASA_URL


def to_rasa(request: RasaRequest):
    r = requests.post(rasaUrl, data=request.json())
    res_obj = json.loads(r.text)
    response: RasaResponse = RasaResponse(recipient_id=res_obj['recipient_id'], text=res_obj['text'], is_correct=res_obj['correct'])

    return response


def parse_user_question(body: RasaRequest):
    response: RasaResponse = to_rasa(body)
    return response
