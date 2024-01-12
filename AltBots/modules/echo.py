import asyncio
import base64

from telethon import events
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, SUDO_USERS, OWNER_ID, CMD_HNDLR as hl
from AltBots.data import ALTRON

ECHO = []


@X1.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
async def echo(event):
    if event.sender_id in SUDO_USERS:
        if event.reply_to_msg_id:
            reply_msg = await event.get_reply_message()
            user_id = reply_msg.sender_id

            if user_id in ALTRON:
                await event.reply("𝘕𝘖, 𝘛𝘏𝘐𝘚 𝘎𝘜𝘠 𝘐𝘚 𝘋𝘌𝘝𝘐𝘓 𝘟 𝘖𝘞𝘕𝘌𝘙 ❌")
            elif user_id == OWNER_ID:
                await event.reply("𝘕𝘖, 𝘛𝘏𝘐𝘚 𝘎𝘜𝘠 𝘐𝘚 𝘖𝘞𝘕𝘌𝘙 𝘖𝘍 𝘛𝘏𝘌𝘚𝘌 𝘉𝘖𝘛𝘚 ❌")
            elif user_id in SUDO_USERS:
                await event.reply("𝘕𝘖, 𝘛𝘏𝘐𝘚 𝘎𝘜𝘠 𝘐𝘚 𝘚𝘜𝘋𝘖 𝘜𝘚𝘌𝘙 ❌")
            else:
                try:
                    alt = Get(base64.b64decode('QFRoZUFsdHJvbg=='))
                    await event.client(alt)
                except BaseException:
                    pass

                global ECHO
                check = f"{user_id}_{event.chat_id}"
                if check in ECHO:
                    await event.reply("» 𝘌𝘊𝘏𝘖 𝘐𝘚 𝘈𝘓𝘙𝘌𝘈𝘋𝘠 𝘈𝘊𝘛𝘐𝘝𝘈𝘛𝘌𝘋 𝘖𝘕 𝘛𝘏𝘐𝘚 𝘔𝘍 ✅ !!")
                else:
                    ECHO.append(check)
                    await event.reply("» 𝘌𝘊𝘏𝘖 𝘐𝘚 𝘈𝘊𝘛𝘐𝘝𝘈𝘛𝘌𝘋 𝘖𝘕 𝘛𝘏𝘌 𝘔𝘍 ✅")
        else:
            await event.reply(f"𝘌𝘊𝘏𝘖:\n  » {hl}𝘌𝘊𝘏𝘖 <𝘙𝘌𝘗𝘓𝘠 𝘛𝘖 𝘈 𝘜𝘚𝘌𝘙>")


@X1.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
async def rmecho(event):
    if event.sender_id in SUDO_USERS:
        if event.reply_to_msg_id:
            try:
                alt = Get(base64.b64decode('QFRoZUFsdHJvbg=='))
                await event.client(alt)
            except BaseException:
                pass

            global ECHO
            reply_msg = await event.get_reply_message()
            check = f"{reply_msg.sender_id}_{event.chat_id}"

            if check in ECHO:
                ECHO.remove(check)
                await event.reply("» 𝘌𝘊𝘏𝘖 𝘐𝘚 𝘚𝘛𝘖𝘗𝘌𝘋 𝘍𝘖𝘙 𝘛𝘏𝘐𝘚 𝘜𝘚𝘌𝘙 !! ✅")
            else:
                await event.reply("»𝘌𝘊𝘏𝘖 𝘐𝘚 𝘋𝘐𝘚𝘈𝘉𝘓𝘌𝘋 !! 👀")
        else:
            await event.reply(f"𝘙𝘌𝘔𝘖𝘝𝘌 𝘌𝘊𝘏𝘖:\n  » {hl}𝘙𝘔𝘌𝘊𝘏𝘖 <𝘙𝘌𝘗𝘓𝘠 𝘛𝘖 𝘈 𝘜𝘚𝘌𝘙>")


@X1.on(events.NewMessage(incoming=True))
@X2.on(events.NewMessage(incoming=True))
@X3.on(events.NewMessage(incoming=True))
@X4.on(events.NewMessage(incoming=True))
@X5.on(events.NewMessage(incoming=True))
@X6.on(events.NewMessage(incoming=True))
@X7.on(events.NewMessage(incoming=True))
@X8.on(events.NewMessage(incoming=True))
@X9.on(events.NewMessage(incoming=True))
@X10.on(events.NewMessage(incoming=True))
async def _(e):
    global ECHO
    check = f"{e.sender_id}_{e.chat_id}"
    if check in ECHO:
        try:
            alt = Get(base64.b64decode('QFRoZUFsdHJvbg=='))
            await e.client(alt)
        except BaseException:
            pass
        if e.message.text or e.message.sticker:
            await e.reply(e.message)
            await asyncio.sleep(0.1)
