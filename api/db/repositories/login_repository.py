import json

from bson import ObjectId, json_util

import config
from db.models.login import Login
from models.login.models import LoginCreate, LoginUpdate


class LoginRepository:
    collection = config.MONGODB_CONNECTION[config.DB_NAME][config.LOGIN_COLLECTION_NAME]

    class Exists:
        pass

    class NotFound:
        pass

    @staticmethod
    def create(req: LoginCreate):
        new_login = Login()
        new_login.session_id = req.session_id
        new_login.login_time = req.login_time
        new_login.logout_time = req.logout_time
        new_login.pass_reset = req.pass_reset
        new_login.pass_upd_dte = req.pass_upd_dte
        new_login.device_type = req.device_type
        new_login.device_ip = req.device_ip

        new_login = dict(new_login)

        if LoginRepository.collection.find_one({'session_id': new_login['session_id']}):
            return LoginRepository.Exists
        else:
            return str(LoginRepository.collection.insert_one(new_login).inserted_id)

    @staticmethod
    def get_by_id(id):
        user = LoginRepository.collection.find_one({'_id': ObjectId(id)})
        if user:
            return json.loads(json_util.dumps(dict(user)))
        return None

    @staticmethod
    def get(field, val):
        user = LoginRepository.collection.find_one({field: val})
        if user:
            return json.loads(json_util.dumps(dict(user)))
        return None

    @staticmethod
    def update(
            id,
            req: LoginUpdate
    ):
        login = LoginRepository.collection.find_one({"_id": ObjectId(id)})
        if not login:
            return None

        new_login = Login()
        new_login.session_id = req.session_id
        new_login.login_time = req.login_time
        new_login.logout_time = req.logout_time
        new_login.pass_reset = req.pass_reset
        new_login.pass_upd_dte = req.pass_upd_dte
        new_login.device_type = req.device_type
        new_login.device_ip = req.device_ip
        new_login = dict(new_login)

        LoginRepository.collection.update_one(
            {'_id': ObjectId(id)},
            {'$set': new_login}
        )
        return True

    @staticmethod
    def delete(id):
        res = LoginRepository.collection.delete_one({'_id': ObjectId(id)})
        if res.deleted_count > 0:
            return True
        return False
