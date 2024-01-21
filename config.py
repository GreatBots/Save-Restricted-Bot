import os

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "")  # ⚠️ Required
    API_HASH  = os.environ.get("API_HASH", "") # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") # ⚠️ Required
    STRING_SESSION = os.environ.get("STRING_SESSION", "") # ⚠️ Required
    DB_URL = os.environ.get("DB_URL", "") # ⚠️ Required
    DB_NAME = os.environ.get("DB_NAME", "TgBotData")
    PORT = int(os.environ.get("PORT", "8080"))
