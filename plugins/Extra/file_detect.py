
from pyrogram import Client, filters
from pyrogram.enums import MessageMediaType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply


@Client.on_message(filters.private & filters.reply)
async def refunc(client, message):
    if (message.reply_to_message.reply_markup) and isinstance(message.reply_to_message.reply_markup, ForceReply):
        new_name = message.text
        await message.delete()
        await message.delete()
        media = await client.get_messages(message.chat.id, message.reply_to_message.id)
        file = media.reply_to_message.document or media.reply_to_message.video or media.reply_to_message.audio
        filename = file.file_name
        types = file.mime_type.split("/")
        mime = types[0]
        mg_id = media.reply_to_message.id
        try:
            out = new_name.split(".")
            out[1]
            out_name = out[-1]
            out_filename = new_name
            await message.reply_to_message.delete()
            if mime == "video":
                markup = InlineKeyboardMarkup([[
                    InlineKeyboardButton(" 𝙳𝙾𝙲𝚄𝙼𝙴𝙽𝚃", callback_data="upload_document"),
                    InlineKeyboardButton(" 𝚅𝙸𝙳𝙴𝙾", callback_data="upload_video")]])
            elif mime == "audio":
                markup = InlineKeyboardMarkup([[InlineKeyboardButton(
                    "𝙳𝙾𝙲𝚄𝙼𝙴𝙽𝚃", callback_data="doc"), InlineKeyboardButton("𝙰𝚄𝙳𝙸𝙾", callback_data="upload_audio")]])
            else:
                markup = InlineKeyboardMarkup(
                    [[InlineKeyboardButton("𝙳𝙾𝙲𝚄𝙼𝙴𝙽𝚃", callback_data="upload_document")]])
            # WarninG -> Please Dont chnage anything after this Line 
            await message.reply_text(f"**Select the output file type**\n**🎞New Name** :- ```{out_filename}```", reply_to_message_id=mg_id, reply_markup=markup)

        except:
            try:
                out = filename.split(".")
                out_name = out[-1]
                out_filename = new_name + "." + out_name
            except:
                await message.reply_to_message.delete()
                await message.reply_text("**𝙴𝚁𝚁𝙾𝚁** :  𝙽𝚘  𝙴𝚡𝚝𝚎𝚗𝚝𝚒𝚘𝚗 𝙸𝚗 𝙵𝚒𝚕𝚎, 𝙽𝚘𝚝 𝚂𝚞𝚙𝚙𝚘𝚛𝚝𝚒𝚗𝚐", reply_to_message_id=mg_id)
                return
            await message.reply_to_message.delete()
            if mime == "video":
                markup = InlineKeyboardMarkup([[InlineKeyboardButton(
                    "𝙳𝙾𝙲𝚄𝙼𝙴𝙽𝚃", callback_data="upload_document"), InlineKeyboardButton("🎥 Video", callback_data="upload_video")]])
            elif mime == "audio":
                markup = InlineKeyboardMarkup([[InlineKeyboardButton(
                    "𝙳𝙾𝙲𝚄𝙼𝙴𝙽𝚃", callback_data="upload_document"), InlineKeyboardButton("🎵 audio", callback_data="upload_audio")]])
            else:
                markup = InlineKeyboardMarkup(
                    [[InlineKeyboardButton("𝙳𝙾𝙲𝚄𝙼𝙴𝙽𝚃", callback_data="upload_document")]])
            # WarninG -> Please Dont chnage anything after this Line 
            await message.reply_text(f"**Select the output file type**\n**🎞New Name** :- ```{out_filename}```",
                                     reply_to_message_id=mg_id, reply_markup=markup)
