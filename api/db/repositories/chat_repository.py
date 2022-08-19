import json

from bson import ObjectId, json_util

import config
from db.models.chat import Chat
from models.chat.models import ChatCreate, ChatUpdate


class ChatRepository:
    collection = config.MONGODB_CONNECTION[config.DB_NAME][config.CHAT_COLLECTION_NAME]

    class Exists:
        pass

    class NotFound:
        pass

    @staticmethod
    def create(req: ChatCreate):
        new_chat = Chat()
        new_chat.user_id = req.user_id
        new_chat.user_name = req.user_name
        new_chat.session_id = req.session_id
        new_chat.chat_input_txt = req.chat_input_txt
        new_chat.chat_out_txt = req.chat_out_txt
        new_chat.chat_out_correct = req.chat_out_correct
        new_chat.chat_out_rating = req.chat_out_rating
        new_chat.chat_input_dte = req.chat_input_dte
        new_chat.chat_out_dte = req.chat_out_dte
        new_chat.chat_server_id = req.chat_server_id
        new_chat.type_name = req.type_name
        new_chat.intent_name = req.intent_name
        new_chat.action_name = req.action_name
        new_chat.rasa_data = req.rasa_data

        new_chat = dict(new_chat)

        if ChatRepository.collection.find_one({'session_id': new_chat['session_id']}):
            return ChatRepository.Exists
        else:
            return str(ChatRepository.collection.insert_one(new_chat).inserted_id)

    @staticmethod
    def get_by_id(id):
        chat = ChatRepository.collection.find_one({'_id': ObjectId(id)})
        if chat:
            return json.loads(json_util.dumps(dict(chat)))
        return None

    @staticmethod
    def get(field, val):
        chat = ChatRepository.collection.find_one({field: val})
        if chat:
            return json.loads(json_util.dumps(dict(chat)))
        return None

    @staticmethod
    def update(
            id,
            req: ChatUpdate
    ):
        login = ChatRepository.collection.find_one({"_id": ObjectId(id)})
        if not login:
            return None

        new_chat = Chat()
        new_chat.user_id = req.user_id
        new_chat.user_name = req.user_name
        new_chat.session_id = req.session_id
        new_chat.chat_input_txt = req.chat_input_txt
        new_chat.chat_out_txt = req.chat_out_txt
        new_chat.chat_out_correct = req.chat_out_correct
        new_chat.chat_out_rating = req.chat_out_rating
        new_chat.chat_input_dte = req.chat_input_dte
        new_chat.chat_out_dte = req.chat_out_dte
        new_chat.chat_server_id = req.chat_server_id
        new_chat.type_name = req.type_name
        new_chat.intent_name = req.intent_name
        new_chat.action_name = req.action_name
        new_chat.rasa_data = req.rasa_data
        new_chat = dict(new_chat)

        ChatRepository.collection.update_one(
            {'_id': ObjectId(id)},
            {'$set': new_chat}
        )
        return True

    @staticmethod
    def delete(id):
        res = ChatRepository.collection.delete_one({'_id': ObjectId(id)})
        if res.deleted_count > 0:
            return True
        return False
