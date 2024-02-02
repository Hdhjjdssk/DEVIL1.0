from telethon import __version__, events, Button

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10


@X1.on(events.NewMessage(pattern="!alive"))
@X2.on(events.NewMessage(pattern="!alive"))
@X3.on(events.NewMessage(pattern="!alive"))
@X4.on(events.NewMessage(pattern="!alive"))
@X5.on(events.NewMessage(pattern="!alive"))
@X6.on(events.NewMessage(pattern="!alive"))
@X7.on(events.NewMessage(pattern="!alive"))
@X7.on(events.NewMessage(pattern="!alive"))
@X8.on(events.NewMessage(pattern="!alive"))
@X9.on(events.NewMessage(pattern="!alive"))
@X10.on(events.NewMessage(pattern="!alive")) 
async def start(event):
        AltBot = await event.client.get_me()
        TEXT = f"╔════❰ **ᴅᴇᴠɪʟ x ɪꜱ ᴀʟɪᴠᴇ 🍁** ❱═❍\n"
        TEXT += f"║╭━━━━━━━━━━━━━━━➣\n"
        TEXT += f"║┣ » **ᴘʏᴛʜᴏɴ 🐍:** `3.11.3`\n"
        TEXT += f"║┣ » **ᴠᴇʀꜱɪᴏɴ ⚙️:** `M3.4`\n"
        TEXT += f"║┣ » **ɢʀᴏᴜᴘ 💫:[˹⏤͟͞〲Dᴇᴠɪʟ˹ARC˼🍷˼](https://t.me/+dKGCo7oumwYwZDNl)**\n"
        TEXT += f"║┣ » **ᴅᴇᴠ 🫂:[˹⏤͟͞〲Dᴇᴠɪʟ 🥀˼](https://t.me/KANU_XD)**\n"
        TEXT += f"║╰━━━━━━━━━━━━━━━➣\n"
        TEXT += f"╚══════════════════❍"
        await event.client.send_file(
                    event.chat_id,
                    "https://telegra.ph/file/2f2b8d40e3f2fa4acdc8f.mp4",
                    caption=TEXT, 
                )
