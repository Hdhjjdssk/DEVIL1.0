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
            event = await e.reply("» 𝓛𝓔𝓐𝓥𝓘𝓝𝓖 🍷...")
            mkl = e.text.split(" ", 1)
            try:
                await event.client(LeaveChannelRequest(int(mkl[1])))
            except Exception as e:
                await event.edit(str(e))
        else:
             if e.is_private:
                  alt = f"**»𝓨𝓞𝓤 𝓒𝓐𝓝'𝓣 𝓓𝓞 𝓣𝓗𝓘𝓢 𝓗𝓔𝓡𝓔 !!**\n\n» {hl}𝓛𝓔𝓐𝓥𝓔 <𝓬𝓱𝓪𝓷𝓷𝓮𝓵/𝓬𝓱𝓪𝓽 𝓲𝓭>\n» {hl}𝓛𝓔𝓐𝓥𝓔 : 𝓣𝓨𝓟𝓔 𝓘𝓝 𝓣𝓗𝓔 𝓖𝓡𝓞𝓤𝓟, 𝓑𝓞𝓣 𝓦𝓘𝓛𝓛 𝓐𝓤𝓣𝓞 𝓛𝓔𝓐𝓥𝓔 𝓣𝓗𝓐𝓣 𝓖𝓡𝓞𝓤𝓟"
                  await e.reply(alt)
             else:
                  event = await e.reply("» 𝓛𝓔𝓐𝓥𝓘𝓝𝓖 🍷...")
                  try:
                      await event.client(LeaveChannelRequest(int(e.chat_id)))
                  except Exception as e:
                      await event.edit(str(e))
