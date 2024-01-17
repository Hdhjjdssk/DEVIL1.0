import sys
import heroku3
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, OWNER_ID, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY, CMD_HNDLR as hl
from os import execl, getenv
from telethon import events
from datetime import datetime


@X1.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
async def alive(e):
    if e.sender_id in SUDO_USERS:
        altron = await e.reply(f"⚡")
        await altron.edit(f"""
**ᴅᴇᴠɪʟ x ɪꜱ ᴀʟɪᴠᴇ 🍷**
**━━━━━━━━━━━━━━━━━━━━**
**ʜɪ 👀** :『**ɪ ᴀᴍ ᴅᴇᴠɪʟ X 🍷**』
┏━━━━━━━━━━━━━━━━━━━
┣•» **ᴘʏᴛʜᴏɴ 🐍:** `3.11.3`
┣•» **ᴠᴇʀꜱɪᴏɴ ⚙️:** `M3.4`
┣•» **ɢʀᴏᴜᴘ 🥂:** [ᴊᴏɪɴ](https://t.me/UNI_INDIA_0008)**
┣•» **ᴅᴇᴠ ⚜️:** [⏤͟͞Ꮴɪʟʟᴀɪɴ](https://t.me/KANU_XD)**
┗━━━━━━━━━━━━━━━━━━━
""")
