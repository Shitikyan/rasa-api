from bson import ObjectId
from schematics.models import Model
from schematics.types import StringType, EmailType


class User(Model):
    id = ObjectId()
    user_email = EmailType(required=True)
    user_name = StringType(required=True)
    user_timezone = StringType(required=True)
    blacklisted = StringType(required=True)


