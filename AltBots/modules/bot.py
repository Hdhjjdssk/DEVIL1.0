import sys
import heroku3

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, OWNER_ID, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY, CMD_HNDLR as hl

from os import execl, getenv
from telethon import events
from datetime import datetime


@X1.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
async def ping(e):
    if e.sender_id in SUDO_USERS:
        start = datetime.now()
        altron = await e.reply(f"✨")
        await asyncio.sleep(0.2)
        end = datetime.now()
        mp = (end - start).microseconds / 1000
        await altron.edit("**.**")
        await asyncio.sleep(0.1)
        await altron.edit("**. .**")
        await asyncio.sleep(0.1)
        await altron.edit("**. . .**")
        await asyncio.sleep(0.1)
        await altron.edit("**. . . .**")
        await asyncio.sleep(0.1)
        await altron.edit("**. . . . .**")
        await asyncio.sleep(0.1)
        await altron.edit("**⚡**")
        await asyncio.sleep(0.2)
        await altron.edit("**POWERING THE DEVIL ⚡🍷**")
        await asyncio.sleep(0.1)
        await altron.edit("**⏤ **")
        await asyncio.sleep(0.1)
        await altron.edit("**⏤͟   **")
        await asyncio.sleep(0.1)
        await altron.edit("**⏤͟͞   **")
        await asyncio.sleep(0.1)
        await altron.edit("**⏤͟͞ 𝘿**")
        await asyncio.sleep(0.1)
        await altron.edit("**⏤͟͞ 𝘿𝙀**")
        await asyncio.sleep(0.1)
        await altron.edit("**⏤͟͞ 𝘿𝙀𝙑**")
        await asyncio.sleep(0.1)
        await altron.edit("**⏤͟͞ 𝘿𝙀𝙑𝙄**")
        await asyncio.sleep(0.1)
        await altron.edit("**⏤͟͞ 𝘿𝙀𝙑𝙄𝙇**")
        await asyncio.sleep(0.1)
        await altron.edit("**⏤͟͞ 𝘿𝙀𝙑𝙄𝙇 🍷**")
        await asyncio.sleep(0.1)
        await altron.edit("**⚡**")
        await asyncio.sleep(0.1)
        await altron.edit("**⏤͟͞ 𝘿𝙀𝙑𝙄𝙇 🍷**")
        await asyncio.sleep(0.1)
        await altron.edit("**⚡**")
        await asyncio.sleep(0.1)
        await altron.edit("**⏤͟͞ 𝘿𝙀𝙑𝙄𝙇 🍷**")
        await asyncio.sleep(0.1)
        await altron.edit("**⚡**")
        await asyncio.sleep(0.1)
        await altron.edit("**⏤͟͞ 𝘿𝙀𝙑𝙄𝙇 🍷**")
        await asyncio.sleep(0.1)
        await altron.edit("**⚡**")
        await asyncio.sleep(0.1)
        await altron.edit("**⏤͟͞ 𝘿𝙀𝙑𝙄𝙇 🍷**")
        await asyncio.sleep(0.1)
        await altron.edit("**🟥🟨🟩**")
        await asyncio.sleep(0.3)
         await altron.edit(f"⏤͟͞ 𝘿𝙀𝙑𝙄𝙇 🍷\n» `{mp} ᴍꜱ`")

@X1.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
async def restart(e):
    if e.sender_id in SUDO_USERS:
        await e.reply(f"`𝘙𝘌𝘚𝘛𝘈𝘙𝘛𝘐𝘕𝘎 𝘉𝘖𝘛 ⌛ ...`")
        try:
            await X1.disconnect()
        except Exception:
            pass
        try:
            await X2.disconnect()
        except Exception:
            pass
        try:
            await X3.disconnect()
        except Exception:
            pass
        try:
            await X4.disconnect()
        except Exception:
            pass
        try:
            await X5.disconnect()
        except Exception:
            pass
        try:
            await X6.disconnect()
        except Exception:
            pass
        try:
            await X7.disconnect()
        except Exception:
            pass
        try:
            await X8.disconnect()
        except Exception:
            pass
        try:
            await X9.disconnect()
        except Exception:
            pass
        try:
            await X10.disconnect()
        except Exception:
            pass

        execl(sys.executable, sys.executable, *sys.argv)


@X1.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
async def addsudo(event):
    if event.sender_id == OWNER_ID:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        sudousers = getenv("SUDO_USERS", default=None)

        ok = await event.reply(f"» __𝘈𝘋𝘋𝘐𝘕𝘎 𝘜𝘚𝘌𝘙 𝘈𝘚 𝘚𝘜𝘋𝘖 🫂 ...__")
        target = ""
        if HEROKU_APP_NAME is not None:
            app = Heroku.app(HEROKU_APP_NAME)
        else:
            await ok.edit("`[HEROKU]:" "\nPlease Setup Your` **HEROKU_APP_NAME**")
            return
        heroku_var = app.config()
        if event is None:
            return
        try:
            reply_msg = await event.get_reply_message()
            target = reply_msg.sender_id
        except:
            await ok.edit("» 𝘙𝘌𝘗𝘓𝘠 𝘛𝘖 𝘈 𝘜𝘚𝘌𝘙 👀 !!")
            return

        if str(target) in sudousers:
            await ok.edit(f"𝘛𝘏𝘐𝘚 𝘜𝘚𝘌𝘙 𝘐𝘚 𝘈𝘓𝘙𝘌𝘈𝘋𝘠 𝘈 𝘚𝘜𝘋𝘖 𝘜𝘚𝘌𝘙 💕 !!")
        else:
            if len(sudousers) > 0:
                newsudo = f"{sudousers} {target}"
            else:
                newsudo = f"{target}"
            await ok.edit(f"» **ɴᴇᴡ ꜱᴜᴅᴏ ᴜꜱᴇʀ**: `{target}`\n» `𝘙𝘌𝘚𝘛𝘈𝘙𝘛𝘐𝘕𝘎 𝘉𝘖𝘛 ⌛ ...`")
            heroku_var["SUDO_USERS"] = newsudo    
    
    elif event.sender_id in SUDO_USERS:
        await event.reply("»𝘚𝘙𝘠, 𝘖𝘕𝘓𝘠 𝘖𝘞𝘕𝘌𝘙 𝘊𝘈𝘕 𝘈𝘊𝘊𝘌𝘚𝘚 𝘛𝘏𝘐𝘚 𝘊𝘔𝘋 🔰 ")
