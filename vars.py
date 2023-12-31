from os import environ
import re
import os

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

SESSION = environ.get("SESSION", "forward bot")
API_ID = int(os.environ.get("API_ID", "13859375"))
API_HASH = os.environ.get("API_HASH", "6ae4ba5fdc4eb0948616585a5bb7ee58")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6899028025:AAEyl_WjRr6nzea-zg1Cs05VSmxp4ehX5Fw")

LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1001924870738"))
PORT = int(environ.get("PORT", "8080"))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '2034319320').split()]
UPSTREAM_REPO = environ.get("UPSTREAM_REPO", "https://github.com/Sridhark01/Forward-bot-beta-new")
DB_URI = environ.get('DB_URI', "mongodb+srv://rename:rename@cluster0.yr0wxh3.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = environ.get('DB_NAME', "cluster0")


