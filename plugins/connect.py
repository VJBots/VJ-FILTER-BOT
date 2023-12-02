from info import *
from utils import *
from client import User 
from pyrogram import Client, filters

@Client.on_message(filters.group & filters.command("connect"))
async def connect(bot, message):
    m=await message.reply("connecting..")
    user = await User.get_me()
    try:
       group     = await get_group(message.chat.id)
       user_id   = group["user_id"] 
       user_name = group["user_name"]
       verified  = group["verified"]
       channels  = group["channels"].copy()
    except :
       return await bot.leave_chat(message.chat.id)  
    if message.from_user.id!=user_id:
       return await m.edit(f"<b>Only {user_name} can use this command</b> 😁")
    if bool(verified)==False:
       return await m.edit("💢 <b>This chat is not verified!\n⭕ use /verify</b>")    
    try:
       channel = int(message.command[-1])
       if channel in channels:
          return await message.reply("💢 <b>This channel is already connected! You Cant Connect Again</b>")
       channels.append(channel)
    except:
       return await m.edit("❌ <b>Incorrect format!\nUse</b> `/connect ChannelID`")    
    try:
       chat   = await bot.get_chat(channel)
       group  = await bot.get_chat(message.chat.id)
       c_link = chat.invite_link
       g_link = group.invite_link
       await User.join_chat(c_link)
    except Exception as e:
       if "The user is already a participant" in str(e):
          pass
       else:
          text = f"❌ <b>Error:</b> `{str(e)}`\n⭕ <b>Make sure I'm admin in that channel & this group with all permissions and {(user.username or user.mention)} is not banned there</b>"
          return await m.edit(text)
    await update_group(message.chat.id, {"channels":channels})
    await m.edit(f"💢 <b>Successfully connected to [{chat.title}]({c_link})!</b>", disable_web_page_preview=True)
    text = f"#NewConnection\n\nUser: {message.from_user.mention}\nGroup: [{group.title}]({g_link})\nChannel: [{chat.title}]({c_link})"
    await bot.send_message(chat_id=LOG_CHANNEL, text=text)


@Client.on_message(filters.group & filters.command("disconnect"))
async def disconnect(bot, message):
    m=await message.reply("Please wait..")   
    try:
       group     = await get_group(message.chat.id)
       user_id   = group["user_id"] 
       user_name = group["user_name"]
       verified  = group["verified"]
       channels  = group["channels"].copy()
    except :
       return await bot.leave_chat(message.chat.id)  
    if message.from_user.id!=user_id:
       return await m.edit(f"Only {user_name} can use this command 😁")
    if bool(verified)==False:
       return await m.edit("This chat is not verified!\nuse /verify")    
    try:
       channel = int(message.command[-1])
       if channel not in channels:
          return await m.edit("<b>You didn't added this channel yet Or Check Channel Id</b>")
       channels.remove(channel)
    except:
       return await m.edit("❌ <b>Incorrect format!\nUse</b> `/disconnect ChannelID`")
    try:
       chat   = await bot.get_chat(channel)
       group  = await bot.get_chat(message.chat.id)
       c_link = chat.invite_link
       g_link = group.invite_link
       await User.leave_chat(channel)
    except Exception as e:
       text = f"❌ <b>Error:</b> `{str(e)}`\n💢 <b>Make sure I'm admin in that channel & this group with all permissions and {(user.username or user.mention)} is not banned there</b>"
       return await m.edit(text)
    await update_group(message.chat.id, {"channels":channels})
    await m.edit(f"💢 <b>Successfully disconnected from [{chat.title}]({c_link})!</b>", disable_web_page_preview=True)
    text = f"#DisConnection\n\nUser: {message.from_user.mention}\nGroup: [{group.title}]({g_link})\nChannel: [{chat.title}]({c_link})"
    await bot.send_message(chat_id=LOG_CHANNEL, text=text)


@Client.on_message(filters.group & filters.command("connections"))
async def connections(bot, message):
    group     = await get_group(message.chat.id)    
    user_id   = group["user_id"]
    user_name = group["user_name"]
    channels  = group["channels"]
    f_sub     = group["f_sub"]
    if message.from_user.id!=user_id:
       return await message.reply(f"<b>Only {user_name} can use this command</b> 😁")
    if bool(channels)==False:
       return await message.reply("<b>This group is currently not connected to any channels!\nConnect one using /connect</b>")
    text = "This Group is currently connected to:\n\n"
    for channel in channels:
        try:
           chat = await bot.get_chat(channel)
           name = chat.title
           link = chat.invite_link
           text += f"🔗<b>Connected Channel - [{name}]({link})</b>\n"
        except Exception as e:
           await message.reply(f"❌ Error in `{channel}:`\n`{e}`")
    if bool(f_sub):
       try:
          f_chat  = await bot.get_chat(channel)
          f_title = f_chat.title
          f_link  = f_chat.invite_link
          text += f"\nFSub: [{f_title}]({f_link})"
       except Exception as e:
          await message.reply(f"❌ <b>Error in FSub</b> (`{f_sub}`)\n`{e}`")
   
    await message.reply(text=text, disable_web_page_preview=True)
