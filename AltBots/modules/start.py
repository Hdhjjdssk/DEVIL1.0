from telethon import __version__, events, Button

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10


START_BUTTON = [
    [
        Button.inline("✦ 𝘊𝘖𝘔𝘔𝘈𝘕𝘋𝘚 ✦", data="help_back")
    ],
    [
        Button.url("✦ 𝘊𝘏𝘈𝘕𝘕𝘌𝘓 ✦", "https://t.me/rasedidstore"),
        Button.url("✦ 𝘚𝘜𝘗𝘗𝘖𝘙𝘛 ✦", "https://t.me/UNI_INDIA_0008")
    ],
    [
        Button.url("✦ 𝘙𝘌𝘗𝘖 ✦", "https://t.me/FriendCastel")
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
        TEXT = f"**𝘏𝘌𝘠 💕​**"
        TEXT = f"**𝘐 𝘈𝘔 𝘋𝘌𝘝𝘐𝘓 𝘟 🍷**"​
        TEXT += f"» **𝘔𝘠 𝘋𝘌𝘝 🫂: [⏤͟͞Ꮴɪʟʟᴀɪɴ [AFK] 🍷](https://t.me/KANU_XD)**\n\n"
        await event.client.send_file(
                    event.chat_id,
                    "https://graph.org/file/37f245cb99eb19233576e.jpg",
                    caption=TEXT, 
                    buttons=START_BUTTON
                )
