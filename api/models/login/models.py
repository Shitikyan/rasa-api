from pydantic import BaseModel


class LoginCreate(BaseModel):
    session_id: str
    login_time: str
    logout_time: str
    pass_reset: bool
    pass_upd_dte: str
    device_type: str
    device_ip: str


class LoginUpdate(BaseModel):
    session_id: str
    login_time: str
    logout_time: str
    pass_reset: bool
    pass_upd_dte: str
    device_type: str
    device_ip: str
