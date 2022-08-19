import json

from bson import ObjectId, json_util

import config
from db.models.user import User
from models.user.models import UserCreate, UserUpdate


class UserRepository:
    collection = config.MONGODB_CONNECTION[config.DB_NAME][config.USER_COLLECTION_NAME]

    class Exists:
        pass

    class NotFound:
        pass

    @staticmethod
    def create(req: UserCreate):
        new_user = User()
        new_user.user_email = req.user_email
        new_user.user_name = req.user_name
        new_user.user_timezone = req.user_timezone
        new_user.blacklisted = req.blacklisted

        new_user = dict(new_user)

        if UserRepository.collection.find_one({'user_email': new_user['user_email']}):
            return UserRepository.Exists
        else:
            return str(UserRepository.collection.insert_one(new_user).inserted_id)

    @staticmethod
    def get_by_id(id):
        user = UserRepository.collection.find_one({'_id': ObjectId(id)})
        if user:
            return json.loads(json_util.dumps(dict(user)))
        return None

    @staticmethod
    def get(field, val):
        user = UserRepository.collection.find_one({field: val})
        if user:
            return json.loads(json_util.dumps(dict(user)))
        return None

    @staticmethod
    def update(
            id,
            req: UserUpdate
    ):
        user = UserRepository.collection.find_one({"_id": ObjectId(id)})
        if not user:
            return None

        new_user = User()
        new_user.user_email = req.user_email
        new_user.user_name = req.user_name
        new_user.user_timezone = req.user_timezone
        new_user.blacklisted = req.blacklisted
        new_user = dict(new_user)

        UserRepository.collection.update_one(
            {'_id': ObjectId(id)},
            {'$set': new_user}
        )
        return True

    @staticmethod
    def delete(id):
        res = UserRepository.collection.delete_one({'_id': ObjectId(id)})
        if res.deleted_count > 0:
            return True
        return False
