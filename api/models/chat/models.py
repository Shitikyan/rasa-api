from pydantic import BaseModel


class ChatCreate(BaseModel):
    user_id: str
    user_name: str
    session_id: str
    chat_input_txt: str
    chat_out_txt: str
    chat_out_correct: str
    chat_out_rating: int
    chat_input_dte: str
    chat_out_dte: str
    chat_server_id: str
    type_name: str
    intent_name: str
    action_name: str
    rasa_data: str


class ChatUpdate(BaseModel):
    user_id: str
    user_name: str
    session_id: str
    chat_input_txt: str
    chat_out_txt: str
    chat_out_correct: str
    chat_out_rating: int
    chat_input_dte: str
    chat_out_dte: str
    chat_server_id: str
    type_name: str
    intent_name: str
    action_name: str
    rasa_data: str
