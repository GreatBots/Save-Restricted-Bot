import os

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "")  # ⚠️ Required
    API_HASH  = os.environ.get("API_HASH", "") # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") # ⚠️ Required
    STRING_SESSION = os.environ.get("STRING_SESSION", "") # ⚠️ Required
    FORCE_SUB = os.config.get("FORCE_SUB", "")
    PORT = int(os.environ.get("PORT", "8080"))
