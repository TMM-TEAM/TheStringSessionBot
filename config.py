from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN")
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

OWNER_ID = int(getenv("OWNER_ID", 5311223486))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/tmm_support_chat")


Must_JOIN = getenv("MUST_JOIN","tmm_heroku_world") 
