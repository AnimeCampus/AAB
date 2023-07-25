from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "19099900"))
    API_HASH = getenv("API_HASH", "2b445de78e5baf012a0793e60bd4fbf5")
    BOT_TOKEN = getenv("BOT_TOKEN", "6655586588:AAGVpTOBW2IflwbS0WOEhAmXfyrUn-DZKVs")
    FSUB = getenv("FSUB", "Anime_Campus")
    CHID = int(getenv("CHID", "-1001453145062"))
    SUDO = list(map(int, getenv("SUDO", "6265459491 6198858059").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://sonu55:sonu55@cluster0.vqztrvk.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()
