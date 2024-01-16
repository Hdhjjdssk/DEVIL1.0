from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, SUDO_USERS, CMD_HNDLR as hl

from telethon import events
from telethon.tl.functions.channels import LeaveChannelRequest


@X1.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
async def leave(e):
    if e.sender_id in SUDO_USERS:

        if len(e.text) > 7:
            event = await e.reply("» 𝘓𝘌𝘈𝘝𝘐𝘕𝘎 ⌛...")
            mkl = e.text.split(" ", 1)
            try:
                await event.client(LeaveChannelRequest(int(mkl[1])))
            except Exception as e:
                await event.edit(str(e))
        else:
             if e.is_private:
                  alt = f"**»𝘠𝘖𝘜 𝘊𝘈𝘕'𝘛 𝘋𝘖 𝘛𝘏𝘐𝘚 𝘏𝘌𝘙𝘌 !!**\n\n» {hl}𝘓𝘌𝘈𝘝𝘌 <𝘊𝘩𝘢𝘯𝘯𝘦𝘭/𝘊𝘩𝘢𝘵 𝘐𝘥 >\n» {hl}𝘓𝘌𝘈𝘝𝘌 : 𝘛𝘠𝘗𝘌 𝘛𝘏𝘐𝘚 𝘐𝘕 𝘎𝘙𝘖𝘜𝘗, 𝘉𝘖𝘛 𝘞𝘐𝘓𝘓 𝘈𝘜𝘛𝘖 𝘓𝘌𝘈𝘝𝘌 𝘛𝘏𝘈𝘛 𝘎𝘙𝘖𝘜𝘗"
                  await e.reply(alt)
             else:
                  event = await e.reply("» 𝘓𝘌𝘈𝘝𝘐𝘕𝘎 ⌛...")
                  try:
                      await event.client(LeaveChannelRequest(int(e.chat_id)))
                  except Exception as e:
                      await event.edit(str(e))
