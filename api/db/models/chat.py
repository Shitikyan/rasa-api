from bson import ObjectId
from schematics.models import Model
from schematics.types import StringType, TimestampType, IntType


class Chat(Model):
    id = ObjectId()
    user_id = StringType()
    user_name = StringType(required=True)
    session_id = StringType()
    chat_input_txt = StringType()
    chat_out_txt = StringType()
    chat_out_correct = StringType()
    chat_out_rating = IntType()
    chat_input_dte = TimestampType()
    chat_out_dte = TimestampType()
    chat_server_id = StringType()
    type_name = StringType()
    intent_name = StringType()
    action_name = StringType()
    rasa_data = StringType()
