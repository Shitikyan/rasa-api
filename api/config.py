from starlette.config import Config

config = Config(".env")

PROJECT_NAME = "Rasa API Server"
VERSION = "1.0.0"
API_PREFIX = "/api"

RASA_URL = config("RASA_URL", cast=str)
