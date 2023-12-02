import asyncio
from .helpers import *
from time import time
from client import DlBot


async def check_up(bot):   
    _time = int(time()) 
    all_data = await get_all_dlt_data(_time)
    for data in all_data:
        try:
           await bot.delete_messages(chat_id=data["chat_id"],
                                     message_ids=data["message_id"])           
        except Exception as e:
           err=data
           err["❌ Error"]=str(e)
           print(err)
    await delete_all_dlt_data(_time)

async def run_check_up():
    async with DlBot as bot: 
        while True:  
           await check_up(bot)
           await asyncio.sleep(1)
    
if __name__=="__main__":   
   asyncio.run(run_check_up())
