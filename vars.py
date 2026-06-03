import os
from os import environ

API_ID = int(environ.get("API_ID", "29136894"))
API_HASH = environ.get("API_HASH", "88f3d07b70de48ac1fc13866b0c9e562")
BOT_TOKEN = environ.get("BOT_TOKEN", "8957567289:AAFPt4Cn2ktjzh9lhp68uVn8XiwbQJgSg1Q")

OWNER = int(environ.get("OWNER", "8938138545"))
CREDIT = environ.get("CREDIT", "CLAT OWNER")
CREDIT_LINK = environ.get("CREDIT_LINK", "https://t.me/CLAT_OWNER")

LOG_CHANNEL = environ.get("LOG_CHANNEL", "-1003711131531")

AUTH_USERS_ENV = environ.get("AUTH_USERS", "8938138545,8494053059")
MONGO_URL = environ.get("MONGO_URL", "")
DATABASE_NAME = environ.get("DATABASE_NAME", "saini")
cookies_file_path = environ.get("cookies_file_path", "youtube_cookies.txt")