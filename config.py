from os import environ 

class Config:
    API_ID = environ.get("API_ID", "25601757")
    API_HASH = environ.get("API_HASH", "fc89773b4cc68c49492af6f3e6fd2cf2")
    BOT_TOKEN = environ.get("BOT_TOKEN", "70955...") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://danigray:P0UJ4P28W1ncOEeV@cluster0.pxupwai.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '8089712530').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
