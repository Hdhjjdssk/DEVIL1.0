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
altron = await message.edit("`⚡`")
await asyncio.sleep(0.3)
ser = (await client.get_me()).mention
upt = get_uptime(time.time())
await altron.edit("`⏤͟͞ ƉɆ⩔ƗⱠ 🍷`")
await asyncio.sleep(0.5)
await altron.edit("`✨`")

       aliver = f"""
╭────────x────────๏
╰๏**ᴅᴇᴠɪʟ X ɪꜱ ᴀʟɪᴠᴇ 💕**
╰๏ **ᴍᴀꜱᴛᴇʀ 🫂 »** {ᴜꜱᴇʀ}
╰๏ **ᴜᴘᴛɪᴍᴇ ⌛ »** `{ᴜᴘᴛ}`
╰────────x────────๏
"""
    await asyncio.sleep(0.3)
    await altron.delete()
    await message.reply_photo(ALIVE_PIC, caption=aliver)

ALIVE_PIC = "https://graph.org/file/c470ed44e1f01628363a2.jpg"
