from telethon import events, Button

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, SUDO_USERS, CMD_HNDLR as hl


HELP_STRING = f"""
╭───────ʜᴇʟᴘ ᴍᴇɴᴜ─────๏
┣𝘋𝘌𝘝𝘐𝘓 𝘟 𝘏𝘌𝘓𝘗 𝘔𝘌𝘕𝘜 🍷💕
┣
┣𝘊𝘓𝘐𝘊𝘒 𝘖𝘕 𝘉𝘌𝘓𝘖𝘞 𝘉𝘜𝘛𝘛𝘖𝘕𝘚 𝘍𝘖𝘙 𝘏𝘌𝘓𝘗 💫
┣
┣𝘋𝘌𝘝 💕: @KANU_XD 🍻
╰──────────乂─────────๏
"""
HELP_BUTTON = [
    [
      Button.inline("❖ 𝘚𝘗𝘈𝘔 ❖", data="spam"),
      Button.inline("❖ 𝘙𝘈𝘐𝘋 ❖", data="raid")
    ],
    [
      Button.inline("❖ 𝘌𝘟𝘛𝘙𝘈 ❖", data="extra"),
      Button.inline("❖ 𝘖𝘞𝘕𝘌𝘙 ❖", data="owner")
    ],
    [
      Button.url("❖ 𝘎𝘙𝘖𝘜𝘗 ❖", "https://t.me/UNI_INDIA_0008")
    ]
  ]


@X1.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):
    if event.sender_id in SUDO_USERS:
        try:
          await event.client.send_file(event.chat_id,
              "https://graph.org/file/7d76c56010dd962ac0dbe.jpg",
              caption=HELP_STRING,
              buttons=HELP_BUTTON
              )
        except Exception as e:
            await event.client.send_message(event.chat_id, f"An Exception Occured!\n\n**ERROR:** {str(e)}")


extra_msg = f"""
**» ᴇ​🇽​ᴛʀᴀ ᴄᴏᴍᴍᴀɴᴅꜱ⦂**

𝗨𝘀𝗲𝗿𝗕𝗼𝘁: **ᴜꜱᴇʀʙᴏᴛ ᴄᴍᴅꜱ**
 ˣ {hl}ᴘɪɴɢ

𝗘𝗰𝗵𝗼: **ᴛᴏ ᴀᴄᴛɪᴠᴇ ᴇᴄʜᴏ ᴏɴ ᴀɴʏ ᴜꜱᴇʀ**
 ˣ {hl}ᴇᴄʜᴏ <ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ>
 ˣ {hl}ʀᴍᴇᴄʜᴏ <ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ>

𝗟𝗲𝗮𝘃𝗲: **ᴛᴏ ʟᴇᴀᴠᴇ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ**
 ˣ {hl}ʟᴇᴀᴠᴇ <ɢʀᴏᴜᴘ/ᴄʜᴀᴛ ɪᴅ>
 ˣ {hl}ʟᴇᴀᴠᴇ : ᴛʏᴘᴇ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ ʙᴏᴛ ᴡɪʟʟ ᴀᴜᴛᴏ ʟᴇᴀᴠᴇ ᴛʜᴀᴛ ɢʀᴏᴜᴘ

MRaid: **ʟᴏᴠᴇ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ.**
 ˣ {hl}ᴍʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ>
 ˣ {hl}ᴍʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ>

SRaid: **ꜱʜᴀʏᴀʀɪ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ.**
 ˣ {hl}ꜱʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ>
 ˣ {hl}ꜱʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ>

CRaid: **ᴀʙᴄᴅ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ.**
 ˣ {hl}ᴄʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ>
 ˣ {hl}ᴄʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ>

𝗛𝗮𝗻𝗴: **ꜱᴘᴀᴍꜱ ʜᴀɴɢɪɴɢ ᴍᴇꜱꜱᴀɢᴇ ꜰᴏʀ ɢɪᴠᴇɴ ᴄᴏᴜɴᴛᴇʀ.**
 ˣ {hl}ʜᴀɴɢ <ᴄᴏᴜɴᴛᴇʀ>

Flirt: **ꜰʟɪʀᴛꜱ ᴡɪᴛʜ ᴛʜᴇ ɢɪᴠᴇ ᴄᴏᴜɴᴛᴇʀ ᴏɴ ᴜꜱᴇʀ**
 ˣ {hl}ꜰʟɪʀᴛ <ᴄᴏᴜɴᴛᴇʀ>

**© @KANU_XD**
"""


owner_msg = f"""
**» ᴏᴡɴᴇʀ ᴄᴏᴍᴍᴀɴᴅꜱ⦂**

𝗨𝘀𝗲𝗿𝗕𝗼𝘁: **ᴜꜱᴇʀʙᴏᴛ ᴄᴍᴅꜱ**
 ˣ {hl}ꜱᴜᴅᴏ <ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ> --> ᴏᴡɴᴇʀ ᴄᴍᴅ
 ˣ {hl}ʟᴏɢꜱ --> ᴏᴡɴᴇʀ ᴄᴍᴅ
 ˣ {hl}ʀᴇʙᴏᴏᴛ

**© @KANU_XD**
"""      
          
raid_msg = f"""
**» ʀᴀɪᴅ ᴄᴏᴍᴍᴀɴᴅꜱ:**

𝗥𝗮𝗶𝗱: **ᴀᴄᴛɪᴠᴀᴛᴇꜱ ʀᴀɪᴅ ᴏɴ ᴀɴʏ ɪɴᴅɪᴠɪᴅᴜᴀʟ ᴜꜱᴇʀ ꜰᴏʀ ɢɪᴠᴇɴ ʀᴀɴɢᴇ.**
 ˣ {hl}ʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ>
 ˣ {hl}ʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ>

𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱: **ᴀᴄᴛɪᴠᴀᴛᴇꜱ ʀᴇᴘʟʏ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ.**
 ˣ {hl}ʀʀᴀɪᴅ <ʀᴇᴘʟʏɪɴɢ ᴛᴏ ᴜꜱᴇʀ>
 ˣ {hl}ʀʀᴀɪᴅ <ᴜꜱᴇʀɴᴀᴍᴇ>

𝗗𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱: **ᴅᴇᴀᴄᴛɪᴠᴀᴛᴇꜱ ʀᴇᴘʟʏ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ.**
 ˣ {hl}ᴅʀʀᴀɪᴅ <ʀᴇᴘʟʏɪɴɢ ᴛᴏ ᴜꜱᴇʀ>
 ˣ {hl}ᴅʀʀᴀɪᴅ <ᴜꜱᴇʀɴᴀᴍᴇ>

**© @KANU_XD**
"""

spam_msg = f"""
**» ꜱᴘᴀᴍ ᴄᴏᴍᴍᴀɴᴅꜱ:**

𝗦𝗽𝗮𝗺: **ꜱᴘᴀᴍꜱ ᴀ ᴍᴇꜱꜱᴀɢᴇ.**
 ˣ {hl}ꜱᴘᴀᴍ <ᴄᴏᴜɴᴛ> <ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ꜱᴘᴀᴍ> (ʏᴏᴜ ᴄᴀɴ ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇꜱꜱᴀɢᴇ ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ʙᴏᴛ ᴛᴏ ʀᴇᴘʟʏ ᴛʜᴀᴛ ᴍᴇꜱꜱᴀɢᴇ ᴀɴᴅ ᴅᴏ ꜱᴘᴀᴍᴍɪɴɢ)
 ˣ {hl}ꜱᴘᴀᴍ <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏɪɴɢ ᴀɴʏ ᴍᴇꜱꜱᴀɢᴇ>

𝗣𝗼𝗿𝗻𝗦𝗽𝗮𝗺: **ᴘᴏʀᴍᴏɢʀᴀᴘʜʏ ꜱᴘᴀᴍ.**
 ˣ {hl}ᴘꜱᴘᴀᴍ <ᴄᴏᴜɴᴛ>

** © @KANU_XD**
"""                     
           
           
@X1.on(events.CallbackQuery(pattern=r"help_back"))
@X2.on(events.CallbackQuery(pattern=r"help_back"))
@X3.on(events.CallbackQuery(pattern=r"help_back"))
@X4.on(events.CallbackQuery(pattern=r"help_back"))
@X5.on(events.CallbackQuery(pattern=r"help_back"))
@X6.on(events.CallbackQuery(pattern=r"help_back"))
@X7.on(events.CallbackQuery(pattern=r"help_back"))
@X8.on(events.CallbackQuery(pattern=r"help_back"))
@X9.on(events.CallbackQuery(pattern=r"help_back"))
@X10.on(events.CallbackQuery(pattern=r"help_back"))
async def helpback(event):
    if event.query.user_id in SUDO_USERS:    
        await event.edit(
            HELP_STRING,
            buttons=[
              [
                Button.inline("❖ 𝘚𝘗𝘈𝘔 ❖", data="spam"),
                Button.inline("❖ 𝘙𝘈𝘐𝘋 ❖", data="raid")
              ],
              [
                Button.inline("❖ 𝘌𝘟𝘛𝘙𝘈 ❖", data="extra"),
                Button.inline("❖ 𝘖𝘞𝘕𝘌𝘙 ❖", data="owner")
              ],
              [
                Button.url("❖ 𝘎𝘙𝘖𝘜𝘗 ❖", "https://t.me/UNI_INDIA_0008")
              ]
            ]
          )
    else:
        await event.answer("𝘔𝘈𝘒𝘌 𝘠𝘖𝘜𝘙 𝘖𝘞𝘕 𝘋𝘌𝘝𝘐𝘓 𝘟 𝘉𝘖𝘛𝘚 !! @KANU_XD", cache_time=0, alert=True)


@X1.on(events.CallbackQuery(pattern=r"spam"))
@X2.on(events.CallbackQuery(pattern=r"spam"))
@X3.on(events.CallbackQuery(pattern=r"spam"))
@X4.on(events.CallbackQuery(pattern=r"spam"))
@X5.on(events.CallbackQuery(pattern=r"spam"))
@X6.on(events.CallbackQuery(pattern=r"spam"))
@X7.on(events.CallbackQuery(pattern=r"spam"))
@X8.on(events.CallbackQuery(pattern=r"spam"))
@X9.on(events.CallbackQuery(pattern=r"spam"))
@X10.on(events.CallbackQuery(pattern=r"spam"))
async def help_spam(event):
    if event.query.user_id in SUDO_USERS:    
        await event.edit(spam_msg,
              buttons=[[Button.inline("< 𝘉𝘈𝘊𝘒", data="help_back"),],],
              ) 
    else:
        await event.answer("𝘔𝘈𝘒𝘌 𝘠𝘖𝘜𝘙 𝘖𝘞𝘕 𝘋𝘌𝘝𝘐𝘓 𝘟 𝘉𝘖𝘛𝘚 !! @KANU_XD", cache_time=0, alert=True)


@X1.on(events.CallbackQuery(pattern=r"raid"))
@X2.on(events.CallbackQuery(pattern=r"raid"))
@X3.on(events.CallbackQuery(pattern=r"raid"))
@X4.on(events.CallbackQuery(pattern=r"raid"))
@X5.on(events.CallbackQuery(pattern=r"raid"))
@X6.on(events.CallbackQuery(pattern=r"raid"))
@X7.on(events.CallbackQuery(pattern=r"raid"))
@X8.on(events.CallbackQuery(pattern=r"raid"))
@X9.on(events.CallbackQuery(pattern=r"raid"))
@X10.on(events.CallbackQuery(pattern=r"raid"))
async def help_raid(event):
    if event.query.user_id in SUDO_USERS:
        await event.edit(raid_msg,
            buttons=[[Button.inline("< 𝘉𝘈𝘊𝘒", data="help_back"),],],
          )
    else:
        await event.answer("𝘔𝘈𝘒𝘌 𝘠𝘖𝘜𝘙 𝘖𝘞𝘕 𝘋𝘌𝘝𝘐𝘓 𝘟 𝘉𝘖𝘛𝘚 !! @KANU_XD", cache_time=0, alert=True)


@X1.on(events.CallbackQuery(pattern=r"extra"))
@X2.on(events.CallbackQuery(pattern=r"extra"))
@X3.on(events.CallbackQuery(pattern=r"extra"))
@X4.on(events.CallbackQuery(pattern=r"extra"))
@X5.on(events.CallbackQuery(pattern=r"extra"))
@X6.on(events.CallbackQuery(pattern=r"extra"))
@X7.on(events.CallbackQuery(pattern=r"extra"))
@X8.on(events.CallbackQuery(pattern=r"extra"))
@X9.on(events.CallbackQuery(pattern=r"extra"))
@X10.on(events.CallbackQuery(pattern=r"extra"))
async def help_extra(event):
    if event.query.user_id in SUDO_USERS:
        await event.edit(extra_msg,
            buttons=[[Button.inline("< 𝘉𝘈𝘊𝘒", data="help_back"),],],
            )
    else:
        await event.answer("𝘔𝘈𝘒𝘌 𝘠𝘖𝘜𝘙 𝘖𝘞𝘕 𝘋𝘌𝘝𝘐𝘓 𝘟 𝘉𝘖𝘛𝘚 !! @KANU_XD", cache_time=0, alert=True)
