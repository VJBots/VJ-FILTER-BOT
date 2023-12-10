from pyrogram import Client, filters
from pyrogram.types import User, Message, Sticker, Document

@Client.on_message(filters.command(["stickerid"]))
async def stickerid(bot, message):   
    if message.reply_to_message.sticker:
       await message.reply(f"**Sticker ID is**  \n `{message.reply_to_message.sticker.file_id}` \n \n ** Unique ID is ** \n\n`{message.reply_to_message.sticker.file_unique_id}`", quote=True)
    else: 
       await message.reply("Oops !! Not a sticker file")


@Client.on_message(filters.private & filters.group & filters.command(["findsticker"]))
async def findsticker(bot, message):  
    try:
        
        txt = await message.reply_text("Validating Sticker ID")
        stickerid = str(message.reply_to_message.text)
        chat_id = str(message.chat.id)
        await txt.delete()
        await bot.send_sticker(chat_id,f"{stickerid}")
     
    except Exception as error:
        txt = await message.reply_text("Not a Valid File ID")
