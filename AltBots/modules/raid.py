import asyncio

from random import choice

from telethon import events

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, SUDO_USERS, OWNER_ID, CMD_HNDLR as hl
from AltBots.data import RAID, REPLYRAID, ALTRON, MRAID, SRAID, CRAID, ALTRON, FLIRT

REPLY_RAID = []


@X1.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
async def raid(e):
    if e.sender_id in SUDO_USERS:
        xraid = e.text.split(" ", 2)

        if len(xraid) == 3:
            entity = await e.client.get_entity(xraid[2])
            uid = entity.id

        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)
            uid = entity.id

        try:
            if uid in ALTRON:
                await e.reply("𝓝𝓞, 𝓣𝓗𝓘𝓢 𝓖𝓤𝓨 𝓘𝓢 𝓓𝓔𝓥𝓘𝓛 𝓧'𝓢 𝓞𝓦𝓝𝓔𝓡 🍷 ")
            elif uid == OWNER_ID:
                await e.reply("𝓝𝓞, 𝓣𝓗𝓘𝓢 𝓖𝓤𝓨 𝓘𝓢 𝓞𝓦𝓝𝓔𝓡 𝓞𝓕 𝓣𝓗𝓔𝓢𝓔 𝓑𝓞𝓣𝓢 🤖")
            elif uid in SUDO_USERS:
                await e.reply("𝓝𝓞, 𝓣𝓗𝓘𝓢 𝓖𝓤𝓨 𝓘𝓢 𝓢𝓤𝓓𝓞 𝓤𝓢𝓔𝓡 🫂")
            else:
                first_name = entity.first_name
                counter = int(xraid[1])
                username = f"[{first_name}](tg://user?id={uid})"
                for _ in range(counter):
                    reply = choice(RAID)
                    caption = f"{username} {reply}"
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.1)
        except (IndexError, ValueError, NameError):
            await e.reply(f"𝓜𝓞𝓓𝓤𝓛𝓔 𝓝𝓐𝓜𝓔: 𝓡𝓐𝓘𝓓\n  » {hl}𝓡𝓐𝓘𝓓 <𝓬𝓸𝓾𝓷𝓽> <𝓾𝓼𝓮𝓻𝓷𝓪𝓶𝓮 𝓸𝓯 𝓾𝓼𝓮𝓻>\n  » {hl}𝓡𝓐𝓘𝓓 <𝓬𝓸𝓾𝓷𝓽> <𝓻𝓮𝓹𝓵𝔂 𝓽𝓸 𝓾𝓼𝓮𝓻>>")
        except Exception as e:
            print(e)


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
async def _(event):
    global REPLY_RAID
    check = f"{event.sender_id}_{event.chat_id}"
    if check in REPLY_RAID:
        await asyncio.sleep(0.1)
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(choice(REPLYRAID)),
            reply_to=event.message.id,
        )


@X1.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
async def rraid(e):
    if e.sender_id in SUDO_USERS:
        mkrr = e.text.split(" ", 1)
        if len(mkrr) == 2:
            entity = await e.client.get_entity(mkrr[1])

        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)

        try:
            user_id = entity.id
            if user_id in ALTRON:
                await e.reply("𝓝𝓞, 𝓣𝓗𝓘𝓢 𝓖𝓤𝓨 𝓘𝓢 𝓓𝓔𝓥𝓘𝓛 𝓧'𝓢 𝓞𝓦𝓝𝓔𝓡 🍷 ")
            elif user_id == OWNER_ID:
                await e.reply("𝓝𝓞, 𝓣𝓗𝓘𝓢 𝓖𝓤𝓨 𝓘𝓢 𝓞𝓦𝓝𝓔𝓡 𝓞𝓕 𝓣𝓗𝓔𝓢𝓔 𝓑𝓞𝓣𝓢 🤖")
            elif user_id in SUDO_USERS:
                await e.reply("𝓝𝓞, 𝓣𝓗𝓘𝓢 𝓖𝓤𝓨 𝓘𝓢 𝓢𝓤𝓓𝓞 𝓤𝓢𝓔𝓡 🫂")
            else:
                global REPLY_RAID
                check = f"{user_id}_{e.chat_id}"
                if check not in REPLY_RAID:
                    REPLY_RAID.append(check)
                await e.reply("» 𝓐𝓒𝓣𝓘𝓥𝓐𝓣𝓔𝓓 𝓡𝓔𝓟𝓛𝓨𝓡𝓐𝓘𝓓 !! ✅")
        except NameError:
            await e.reply(f"𝓜𝓞𝓓𝓤𝓛𝓔 𝓝𝓐𝓜𝓔: 𝓡𝓔𝓟𝓛𝓨 𝓡𝓐𝓘𝓓\n  » {hl}𝓡𝓡𝓐𝓘𝓓 <𝓾𝓼𝓮𝓻𝓷𝓪𝓶𝓮 𝓸𝓯 𝓾𝓼𝓮𝓻>\n  » {hl}𝓡𝓡𝓐𝓘𝓓 <𝓻𝓮𝓹𝓵𝔂 𝓽𝓸 𝓾𝓼𝓮𝓻>")


@X1.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
async def drraid(e):
    if e.sender_id in SUDO_USERS:
        text = e.text.split(" ", 1)

        if len(text) == 2:
            entity = await e.client.get_entity(text[1])
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)

        try:
            check = f"{entity.id}_{e.chat_id}"
            global REPLY_RAID
            if check in REPLY_RAID:
                REPLY_RAID.remove(check)
            await e.reply("» 𝓡𝓔𝓟𝓛𝓨 𝓡𝓐𝓘𝓓 𝓓𝓔-𝓐𝓒𝓣𝓘𝓥𝓐𝓣𝓔𝓓 !! ✅")
        except NameError:
            await e.reply(f"𝓜𝓞𝓓𝓤𝓛𝓔 𝓝𝓐𝓜𝓔: 𝓓𝓡𝓔𝓟𝓛𝓨𝓡𝓐𝓘𝓓\n  » {hl}𝓓𝓡𝓡𝓐𝓘𝓓 <𝓾𝓼𝓮𝓻𝓷𝓪𝓶𝓮 𝓸𝓯 𝓾𝓼𝓮𝓻>\n  » {hl}𝓓𝓡𝓡𝓐𝓘𝓓 <𝓻𝓮𝓹𝓵𝔂 𝓽𝓸 𝓾𝓼𝓮𝓻>")


@X1.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
async def mraid(e):
    if e.sender_id in SUDO_USERS:
        xraid = e.text.split(" ", 2)

        if len(xraid) == 3:
            entity = await e.client.get_entity(xraid[2])
            uid = entity.id

        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)
            uid = entity.id

        try:
            first_name = entity.first_name
            counter = int(xraid[1])
            username = f"[{first_name}](tg://user?id={uid})"
            for _ in range(counter):
                reply = choice(MRAID)
                caption = f"{username} {reply}"
                await e.client.send_message(e.chat_id, caption)
                await asyncio.sleep(0.1)
        except (IndexError, ValueError, NameError):
            await e.reply(f"𝓜𝓞𝓓𝓤𝓛𝓔 𝓝𝓐𝓜𝓔: 𝓜𝓡𝓐𝓘𝓓\n  » {hl}𝓜𝓡𝓐𝓘𝓓 <𝓬𝓸𝓾𝓷𝓽> <𝓾𝓼𝓮𝓻𝓷𝓪𝓶𝓮 𝓸𝓯 𝓾𝓼𝓮𝓻>\n  » {hl}𝓜𝓡𝓐𝓘𝓓 <𝓬𝓸𝓾𝓷𝓽> <𝓻𝓮𝓹𝓵𝔂 𝓽𝓸 𝓾𝓼𝓮𝓻>")
        except Exception as e:
            print(e)


@X1.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
async def sraid(e):
     if e.sender_id in SUDO_USERS:
        xraid = e.text.split(" ", 2)

        if len(xraid) == 3:
            entity = await e.client.get_entity(xraid[2])
            uid = entity.id

        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)
            uid = entity.id

        try:
            first_name = entity.first_name
            counter = int(xraid[1])
            username = f"[{first_name}](tg://user?id={uid})"
            for _ in range(counter):
                reply = choice(SRAID)
                caption = f"{username} {reply}"
                await e.client.send_message(e.chat_id, caption)
                await asyncio.sleep(0.1)
        except (IndexError, ValueError, NameError):
            await e.reply(f"𝓜𝓞𝓓𝓤𝓛𝓔 𝓝𝓐𝓜𝓔: 𝓢𝓡𝓐𝓘𝓓\n  » {hl}𝓢𝓡𝓐𝓘𝓓 <𝓬𝓸𝓾𝓷𝓽> <𝓾𝓼𝓮𝓻𝓷𝓪𝓶𝓮 𝓸𝓯 𝓾𝓼𝓮𝓻>\n  » {hl}𝓢𝓡𝓐𝓘𝓓 <𝓬𝓸𝓾𝓷𝓽> <𝓻𝓮𝓹𝓵𝔂 𝓽𝓸 𝓾𝓼𝓮𝓻>")
        except Exception as e:
            print(e)


@X1.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
async def craid(e):
    if e.sender_id in SUDO_USERS:
        xraid = e.text.split(" ", 2)

        if len(xraid) == 3:
            entity = await e.client.get_entity(xraid[2])
            uid = entity.id

        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)
            uid = entity.id

        try:
            if uid in ALTRON:
                await e.reply("𝓝𝓞, 𝓣𝓗𝓘𝓢 𝓖𝓤𝓨 𝓘𝓢 𝓓𝓔𝓥𝓘𝓛 𝓧'𝓢 𝓞𝓦𝓝𝓔𝓡 🍷")
            elif uid == OWNER_ID:
                await e.reply("𝓝𝓞, 𝓣𝓗𝓘𝓢 𝓖𝓤𝓨 𝓘𝓢 𝓞𝓦𝓝𝓔𝓡 𝓞𝓕 𝓣𝓗𝓔𝓢𝓔 𝓑𝓞𝓣𝓢 🤖")
            elif uid in SUDO_USERS:
                await e.reply("𝓝𝓞, 𝓣𝓗𝓘𝓢 𝓖𝓤𝓨 𝓘𝓢 𝓢𝓤𝓓𝓞 𝓤𝓢𝓔𝓡 🫂")
            else:
                first_name = entity.first_name
                counter = int(xraid[1])
                username = f"[{first_name}](tg://user?id={uid})"
                for _ in range(counter):
                    reply = choice(CRAID)
                    caption = f"{username} {reply}"
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.1)
        except (IndexError, ValueError, NameError):
            await e.reply(f"𝓜𝓞𝓓𝓤𝓛𝓔 𝓝𝓐𝓜𝓔: 𝓒𝓡𝓐𝓘𝓓\n  » {hl}𝓒𝓡𝓐𝓘𝓓 <𝓬𝓸𝓾𝓷𝓽> <𝓾𝓼𝓮𝓻𝓷𝓪𝓶𝓮 𝓸𝓯 𝓾𝓼𝓮𝓻>\n  » {hl}𝓒𝓡𝓐𝓘𝓓 <𝓬𝓸𝓾𝓷𝓽> <𝓻𝓮𝓹𝓵𝔂 𝓽𝓸 𝓾𝓼𝓮𝓻>")
        except Exception as e:
            print(e)


@X1.on(events.NewMessage(incoming=True, pattern=r"\%sflirt(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%sflirt(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%slirt(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%sflirt(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%sflirt(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%sflirt(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%sflirt(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%sflirt(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%sflirt(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%sflirt(?: |$)(.*)" % hl))
async def flirt(e):
     if e.sender_id in SUDO_USERS:
        xraid = e.text.split(" ", 2)

        if len(xraid) == 3:
            entity = await e.client.get_entity(xraid[2])
            uid = entity.id

        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)
            uid = entity.id

        try:
            first_name = entity.first_name
            counter = int(xraid[1])
            username = f"[{first_name}](tg://user?id={uid})"
            for _ in range(counter):
                reply = choice(FLIRT)
                caption = f"{username} {reply}"
                await e.client.send_message(e.chat_id, caption)
                await asyncio.sleep(0.1)
        except (IndexError, ValueError, NameError):
            await e.reply(f"𝓜𝓞𝓓𝓤𝓛𝓔 𝓝𝓐𝓜𝓔: flirt\n  » {hl}𝓢𝓡𝓐𝓘𝓓 <𝓬𝓸𝓾𝓷𝓽> <𝓾𝓼𝓮𝓻𝓷𝓪𝓶𝓮 𝓸𝓯 𝓾𝓼𝓮𝓻>\n  » {hl}𝓢𝓡𝓐𝓘𝓓 <𝓬𝓸𝓾𝓷𝓽> <𝓻𝓮𝓹𝓵𝔂 𝓽𝓸 𝓾𝓼𝓮𝓻>")
        except Exception as e:
            print(e)
