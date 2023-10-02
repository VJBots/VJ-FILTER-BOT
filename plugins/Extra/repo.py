# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import logging
import os
import requests
from pyrogram import Client, filters


@Client.on_message(filters.command('repo'))
async def git(Kashmira, message):
    pablo = await message.reply_text("`Processing...`")
    args = message.text.split(None, 1)[1]
    if len(message.command) == 1:
        await pablo.edit("No input found")
        return
    r = requests.get("https://api.github.com/search/repositories", params={"q": args})
    lool = r.json()
    if lool.get("total_count") == 0:
        await pablo.edit("File not found")
        return
    else:
        lol = lool.get("items")
        qw = lol[0]
        txt = f"""
<b>Name :</b> <i>{qw.get("name")}</i>

<b>Full Name :</b> <i>{qw.get("full_name")}</i>

<b>Link :</b> {qw.get("html_url")}

<b>Fork Count :</b> <i>{qw.get("forks_count")}</i>

<b>Open Issues :</b> <i>{qw.get("open_issues")}</i>

<b>Powed by :</b> @creatorrio

"""
        if qw.get("description"):
            txt += f'<b>Description :</b> <code>{qw.get("description")}</code>'

        if qw.get("language"):
            txt += f'<b>Language :</b> <code>{qw.get("language")}</code>'

        if qw.get("size"):
            txt += f'<b>Size :</b> <code>{qw.get("size")}</code>'

        if qw.get("score"):
            txt += f'<b>Score :</b> <code>{qw.get("score")}</code>'

        if qw.get("created_at"):
            txt += f'<b>Created At :</b> <code>{qw.get("created_at")}</code>'

        if qw.get("archived") == True:
            txt += f"<b>This Project is Archived</b>"
        await pablo.edit(txt, disable_web_page_preview=True)
