from pydantic import BaseModel


class UserCreate(BaseModel):
    user_email: str
    user_name: str
    user_timezone: str
    blacklisted: str


class UserUpdate(BaseModel):
    user_email: str
    user_name: str
    user_timezone: str
    blacklisted: str