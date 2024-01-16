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
                "𝘍𝘐𝘙𝘚𝘛 𝘚𝘌𝘛 𝘛𝘏𝘌𝘚𝘌 𝘝𝘈𝘙𝘚 𝘐𝘕 𝘏𝘌𝘙𝘜𝘒𝘜 :  `HEROKU_API_KEY` And `HEROKU_APP_NAME`.",
            )
            return

        try:
            Heroku = heroku3.from_key(HEROKU_API_KEY)
            app = Heroku.app(HEROKU_APP_NAME)
        except BaseException:
            await legend.reply(
                "𝘔𝘈𝘒𝘌 𝘚𝘜𝘙𝘌 𝘠𝘖𝘜𝘙 𝘏𝘌𝘙𝘜𝘒𝘜 𝘒𝘌𝘠 & 𝘈𝘗𝘗 𝘕𝘈𝘔𝘌 𝘈𝘙𝘌 𝘊𝘖𝘕𝘍𝘐𝘎𝘜𝘙𝘌𝘋 𝘊𝘖𝘙𝘙𝘌𝘊𝘛𝘓𝘠 𝘐𝘕 𝘏𝘌𝘙𝘜𝘒𝘜"
            )
            return

        logs = app.get_log()
        start = datetime.now()
        fetch = await legend.reply(f"𝘍𝘌𝘛𝘊𝘏𝘐𝘕𝘎 𝘓𝘖𝘎𝘚 📄...")
    
        with open("AltLogs.txt", "w") as logfile:
            logfile.write("𝙳𝙴𝚅𝙸𝙻 𝚇 🍷 [ Bot Logs ]\n\n" + logs)

        end = datetime.now()
        ms = (end-start).seconds
        await asyncio.sleep(1)

        try:
            await X1.send_file(legend.chat_id, "𝘓𝘖𝘎𝘚.𝘛𝘟𝘛", caption=f"⚡ **𝘋𝘌𝘝𝘐𝘓 𝘟 𝘓𝘖𝘎𝘚 🍷** ⚡\n  » **𝘛𝘐𝘔𝘌 𝘛𝘈𝘒𝘌𝘕 ⌛:** `{ms} 𝘚𝘌𝘊𝘖𝘕𝘋𝘚`")
            await fetch.delete()
        except Exception as e:
            await fetch.edit(f"𝘈𝘕 𝘌𝘙𝘖𝘙𝘙 𝘖𝘊𝘊𝘜𝘙𝘙𝘌𝘋 ! \n\n**𝘌𝘙𝘖𝘙𝘙:** {str(e)}")

    elif legend.sender_id in SUDO_USERS:
        await legend.reply("»𝘚𝘙𝘠, 𝘖𝘕𝘓𝘠 𝘖𝘞𝘕𝘌𝘙 𝘊𝘈𝘕 𝘈𝘊𝘊𝘌𝘚𝘚 𝘛𝘏𝘐𝘚 𝘊𝘔𝘋 🤖 ")
