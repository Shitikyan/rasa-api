from schematics.models import Model
from bson import ObjectId
from schematics.types import StringType, TimestampType, BooleanType, IPv4Type


class Login(Model):
    id = ObjectId()
    session_id = StringType()
    login_time = TimestampType(required=True)
    logout_time = TimestampType(required=True)
    pass_reset = BooleanType(required=True)
    pass_upd_dte = TimestampType(required=True)
    device_type = StringType(required=True)
    device_ip = IPv4Type(required=True)
