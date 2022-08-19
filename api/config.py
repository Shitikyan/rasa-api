from pymongo import MongoClient
from starlette.config import Config

config = Config(".env")

PROJECT_NAME = "Rasa API Server"
VERSION = "1.0.0"
API_PREFIX = "/api"

RASA_URL = config("RASA_URL", cast=str)
MONGODB_HOST = config("MONGODB_HOST", cast=str)
MONGODB_PORT = config("MONGODB_PORT", cast=int)
DB_NAME = config("DB_NAME", cast=str)
USER_COLLECTION_NAME = config("USER_COLLECTION_NAME", cast=str)
LOGIN_COLLECTION_NAME = config("LOGIN_COLLECTION_NAME", cast=str)
CHAT_COLLECTION_NAME = config("CHAT_COLLECTION_NAME", cast=str)

MONGODB_CONNECTION = MongoClient(MONGODB_HOST, MONGODB_PORT)
