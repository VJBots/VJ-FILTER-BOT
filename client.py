from info import *
from pyrogram import Client
from subprocess import Popen

User = Client(name="user", session_string=SESSION)
DlBot = Client(name="auto-delete", 
               api_id=API_ID,
               api_hash=API_HASH,           
               bot_token=BOT_TOKEN)

class Bot(Client):   
    def __init__(self):
        super().__init__(   
           "bot",
            api_id=API_ID,
            api_hash=API_HASH,           
            bot_token=BOT_TOKEN,
            plugins={"root": "plugins"})
    async def start(self):                        
        await super().start()        
        await User.start()
        Popen("python3 -m utils.delete", shell=True)       
        print("Bot Started 🔧 Powered By @VJ_Botz")   
    async def stop(self, *args):
        await super().stop()
