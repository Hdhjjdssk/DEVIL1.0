from telethon import __version__, events, Button

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10


START_BUTTON = [
    [
        Button.inline("• 𝓒𝓞𝓜𝓜𝓐𝓝𝓓𝓢 •", data="𝓱𝓮𝓵𝓹_𝓫𝓪𝓬𝓴")
    ],
    [
        Button.url("• 𝓒𝓗𝓐𝓝𝓝𝓔𝓛 •", "https://t.me/Lucky9486"),
        Button.url("• 𝓢𝓤𝓟𝓟𝓞𝓡𝓣 •", "https://t.me/FriendCastel")
    ],
    [
        Button.url("• 𝓡𝓔𝓟𝓞 •", "ᴛʜɪꜱ ɪꜱ ᴄᴜꜱᴛᴏᴍ ʙᴏᴛ 🤖 ᴍᴀᴅᴇ ʙʏ | ᴠɪʟʟᴀɪɴ - ᴀʀᴄ 🍷| ᴊᴏɪɴ ʜᴇʀᴇ ꜰᴏʀ ᴍᴏʀᴇ @FriendCastel")
    ]
]


@X1.on(events.NewMessage(pattern="/start"))
@X2.on(events.NewMessage(pattern="/start"))
@X3.on(events.NewMessage(pattern="/start"))
@X4.on(events.NewMessage(pattern="/start"))
@X5.on(events.NewMessage(pattern="/start"))
@X6.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X8.on(events.NewMessage(pattern="/start"))
@X9.on(events.NewMessage(pattern="/start"))
@X10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
        AltBot = await event.client.get_me()
        bot_name = AltBot.first_name
        bot_id = AltBot.id
        TEXT = f"*𝓜𝓐𝓢𝓣𝓔𝓡​ 🍷 [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\n 𝓘 𝓐𝓜 [{bot_name}](tg://user?id={bot_id})​*\n━━━━━━━━━━━━━━━━━━━\n\n"
        TEXT += f"» *𝓜𝓨 𝓓𝓔𝓥𝓔𝓛𝓞𝓟𝓔𝓡 🍁​ :(https://t.me/VILLAIN_0008)*\n\n"
        TEXT += f"» *𝓓𝓔𝓥𝓘𝓛 𝓧 𝓥𝓔𝓡𝓢𝓘𝓞𝓝 🤖 :* `M3.3`\n"
        TEXT += f"» *𝓟𝓨𝓣𝓗𝓞𝓝 𝓥𝓔𝓡𝓢𝓘𝓞𝓝 🐍 :* `3.11.3`\n"
        TEXT += f"» *𝓣𝓔𝓛𝓔𝓣𝓗𝓞𝓝 𝓥𝓔𝓡𝓢𝓘𝓞𝓝 👀 :* `{__version__}`\n━━━━━━━━━━━━━━━━━"
        await event.client.send_file(
                    event.chat_id,
                    "https://graph.org/file/b49339173b6ad3480d65f.jpg",
                    caption=TEXT, 
                    buttons=START_BUTTON
                )
