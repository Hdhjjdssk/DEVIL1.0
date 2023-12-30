import asyncio
import heroku3

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, SUDO_USERS, OWNER_ID, HEROKU_API_KEY, HEROKU_APP_NAME, CMD_HNDLR as hl

from datetime import datetime

from telethon import events
from telethon.errors import ForbiddenError

 
@X1.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
async def logs(legend):
    if legend.sender_id == OWNER_ID:
        if (HEROKU_APP_NAME is None) or (HEROKU_API_KEY is None):
            await legend.reply(
                legend.chat_id,
                "𝓕𝓲𝓻𝓼𝓽 𝓢𝓮𝓽 𝓣𝓱𝓮𝓼𝓮 𝓥𝓪𝓻𝓼 𝓘𝓷 𝓗𝓮𝓻𝓸𝓴𝓾 :  `HEROKU_API_KEY` And `HEROKU_APP_NAME`.",
            )
            return

        try:
            Heroku = heroku3.from_key(HEROKU_API_KEY)
            app = Heroku.app(HEROKU_APP_NAME)
        except BaseException:
            await legend.reply(
                "𝓜𝓪𝓴𝓮 𝓢𝓾𝓻𝓮 𝓨𝓸𝓾𝓻 𝓗𝓮𝓻𝓸𝓴𝓾 𝓐𝓟𝓘 𝓚𝓮𝔂 & 𝓐𝓹𝓹 𝓝𝓪𝓶𝓮 𝓐𝓻𝓮 𝓒𝓸𝓷𝓯𝓲𝓰𝓾𝓻𝓮𝓭 𝓒𝓸𝓻𝓻𝓮𝓬𝓽𝓵𝔂 𝓘𝓷 𝓗𝓮𝓻𝓸𝓴𝓾"
            )
            return

        logs = app.get_log()
        start = datetime.now()
        fetch = await legend.reply(f"__𝓕𝓮𝓽𝓬𝓱𝓲𝓷𝓰 𝓛𝓸𝓰𝓼 🍷...__")
    
        with open("AltLogs.txt", "w") as logfile:
            logfile.write("𝓓𝓔𝓥𝓘𝓛 𝓧 🍷 [ Bot Logs ]\n\n" + logs)

        end = datetime.now()
        ms = (end-start).seconds
        await asyncio.sleep(1)

        try:
            await X1.send_file(legend.chat_id, "𝓛𝓞𝓖𝓢.𝓽𝔁𝓽", caption=f"⚡ **𝓓𝓔𝓥𝓘𝓛 𝓧 𝓛𝓞𝓖𝓢 🍷** ⚡\n  » **𝓣𝓘𝓜𝓔 𝓣𝓐𝓚𝓔𝓝 ⌛:** `{ms} 𝓢𝓔𝓒𝓞𝓝𝓓𝓢`")
            await fetch.delete()
        except Exception as e:
            await fetch.edit(f"𝓐𝓷 𝓔𝔁𝓬𝓮𝓹𝓽𝓲𝓸𝓷 𝓞𝓬𝓬𝓾𝓻𝓮𝓭 ! \n\n**𝓔𝓡𝓡𝓞𝓡:** {str(e)}")

    elif legend.sender_id in SUDO_USERS:
        await legend.reply("»𝓢𝓞𝓡𝓡𝓨, 𝓞𝓝𝓛𝓨 𝓞𝓦𝓝𝓔𝓡 𝓒𝓐𝓝 𝓐𝓒𝓒𝓔𝓢𝓢 𝓣𝓗𝓘𝓢 𝓒𝓞𝓜𝓜𝓐𝓝𝓓 🤖 ")
