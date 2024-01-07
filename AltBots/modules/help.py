from telethon import events, Button

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, SUDO_USERS, CMD_HNDLR as hl


HELP_STRING = f"𝓓𝓔𝓥𝓘𝓛 𝓧 𝓗𝓔𝓛𝓟 𝓜𝓔𝓝𝓤 🍷\n\n» **𝓒𝓛𝓘𝓒𝓚 𝓞𝓝 𝓑𝓔𝓛𝓞𝓦 𝓑𝓤𝓣𝓣𝓞𝓝𝓢 𝓕𝓞𝓡 𝓗𝓔𝓛𝓟**\n» **𝓓𝓔𝓥𝓔𝓛𝓞𝓟𝓔𝓡: KUNAL 🍷**"

HELP_BUTTON = [
    [
      Button.inline("• 𝓢𝓟𝓐𝓜 •", data="spam"),
      Button.inline("• 𝓡𝓐𝓘𝓓 •", data="raid")
    ],
    [
      Button.inline("• 𝓔𝓧𝓣𝓡𝓐 •", data="extra")
    ],
    [
      Button.url("• 𝓖𝓡𝓞𝓤𝓟 •", "https://t.me/FriendCastel"),
      Button.url("• 𝓢𝓤𝓟𝓟𝓞𝓡𝓣 •", "https://t.me/UNI_INDIA_0008")
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
              "https://graph.org/file/b47ffa55d5c3c3d9b047b.jpg",
              caption=HELP_STRING,
              buttons=HELP_BUTTON
              )
        except Exception as e:
            await event.client.send_message(event.chat_id, f"𝓐𝓝 𝓔𝓧𝓒𝓔𝓟𝓣𝓘𝓞𝓝 𝓞𝓒𝓒𝓤𝓡𝓔𝓓 !\n\n**𝓔𝓡𝓡𝓞𝓡:** {str(e)}")


extra_msg = f"""
**» 
𝓔𝓧𝓣𝓡𝓐 𝓒𝓞𝓜𝓜𝓐𝓝𝓓 👾:**

𝓤𝓢𝓔𝓡𝓑𝓞𝓣: **𝓤𝓢𝓔𝓡𝓑𝓞𝓣 𝓒𝓜𝓓𝓢**
  1) {hl}𝓟𝓘𝓝𝓖
  2) {hl}𝓡𝓔𝓑𝓞𝓞𝓣
  3) {hl}𝓢𝓤𝓓𝓞 <𝓻𝓮𝓹𝓵𝔂 𝓽𝓸 𝓾𝓼𝓮𝓻> --> 𝓞𝓦𝓝𝓔𝓡 𝓒𝓜𝓓
  4) {hl}𝓛𝓞𝓖𝓢 --> 𝓞𝓦𝓝𝓔𝓡 𝓒𝓜𝓓

𝓔𝓒𝓗𝓞: **𝓣𝓞 𝓐𝓒𝓣𝓘𝓥𝓐𝓣𝓔 𝓔𝓒𝓗𝓞 𝓞𝓝 𝓐𝓝𝓨 𝓤𝓢𝓔𝓡**
  1) {hl}𝓔𝓒𝓗𝓞 <𝓻𝓮𝓹𝓵𝔂 𝓽𝓸 𝓾𝓼𝓮𝓻>
  2) {hl}𝓡𝓜𝓔𝓒𝓗𝓞 <𝓻𝓮𝓹𝓵𝔂 𝓽𝓸 𝓾𝓼𝓮𝓻>

𝓛𝓔𝓐𝓥𝓔: **𝓣𝓞 𝓛𝓔𝓐𝓥𝓔 𝓖𝓡𝓞𝓤𝓟**
  1) {hl}𝓛𝓔𝓐𝓥𝓔 <𝓰𝓻𝓸𝓾𝓹/𝓬𝓱𝓪𝓽 𝓲𝓭>
  2) {hl}𝓛𝓔𝓐𝓥𝓔 : 𝓣𝓨𝓟𝓔 𝓘𝓝 𝓣𝓗𝓔 𝓖𝓡𝓞𝓤𝓟 𝓑𝓞𝓣 𝓦𝓘𝓛𝓛 𝓐𝓤𝓣𝓞 𝓛𝓔𝓐𝓥𝓔 𝓣𝓗𝓐𝓣 𝓖𝓡𝓞𝓤𝓟


**@rasedidstore**
"""

                 
raid_msg = f"""
**» 𝓡𝓐𝓘𝓓 𝓒𝓞𝓜𝓜𝓐𝓝𝓓𝓢:**

𝓡𝓐𝓘𝓓: **𝓐𝓒𝓣𝓘𝓥𝓐𝓣𝓔𝓢 𝓡𝓐𝓘𝓓 𝓞𝓝 𝓐𝓝𝓨 𝓘𝓝𝓓𝓘𝓥𝓘𝓓𝓤𝓐𝓛 𝓤𝓢𝓔𝓡 𝓕𝓞𝓡 𝓖𝓘𝓥𝓔𝓝 𝓡𝓐𝓝𝓖𝓔**
  1) {hl}𝓡𝓐𝓘𝓓 <𝓬𝓸𝓾𝓷𝓽> <𝓾𝓼𝓮𝓻𝓷𝓪𝓶𝓮>
  2) {hl}𝓡𝓐𝓘𝓓 <𝓬𝓸𝓾𝓷𝓽> <𝓻𝓮𝓹𝓵𝔂 𝓽𝓸 𝓾𝓼𝓮𝓻>

𝓡𝓔𝓟𝓛𝓨 𝓡𝓐𝓘𝓓: **𝓐𝓒𝓣𝓘𝓥𝓐𝓣𝓔𝓢 𝓡𝓔𝓟𝓛𝓨 𝓡𝓐𝓘𝓓 𝓞𝓝 𝓤𝓢𝓔𝓡**
  1) {hl}𝓡𝓡𝓐𝓘𝓓 <𝓻𝓮𝓹𝓵𝔂𝓲𝓷𝓰 𝓽𝓸 𝓾𝓼𝓮𝓻>
  2) {hl}𝓡𝓡𝓐𝓘𝓓 <𝓾𝓼𝓮𝓻𝓷𝓪𝓶𝓮>

𝓓𝓡𝓔𝓟𝓛𝓨 𝓡𝓐𝓘𝓓: **𝓓𝓔𝓐𝓒𝓣𝓘𝓥𝓐𝓣𝓔𝓢 𝓡𝓔𝓟𝓛𝓨 𝓡𝓐𝓘𝓓 𝓞𝓝 𝓤𝓢𝓔𝓡**
  1) {hl}𝓓𝓡𝓡𝓐𝓘𝓓 <𝓻𝓮𝓹𝓵𝔂𝓲𝓷𝓰 𝓽𝓸 𝓾𝓼𝓮𝓻>
  2) {hl}𝓓𝓡𝓡𝓐𝓘𝓓 <𝓾𝓼𝓮𝓻𝓷𝓪𝓶𝓮>

𝓜𝓡𝓐𝓘𝓓: **𝓛𝓞𝓥𝓔 𝓡𝓐𝓘𝓓 𝓞𝓝 𝓤𝓢𝓔𝓡**
  1) {hl}𝓜𝓡𝓐𝓘𝓓 <𝓬𝓸𝓾𝓷𝓽> <𝓾𝓼𝓮𝓻𝓷𝓪𝓶𝓮>
  2) {hl}𝓜𝓡𝓐𝓘𝓓 <𝓬𝓸𝓾𝓷𝓽> <𝓻𝓮𝓹𝓵𝔂 𝓽𝓸 𝓾𝓼𝓮𝓻>

𝓢𝓡𝓐𝓘𝓓: **𝓢𝓗𝓐𝓨𝓐𝓡𝓘 𝓡𝓐𝓘𝓓 𝓞𝓝 𝓤𝓢𝓔𝓡**
  1) {hl}𝓢𝓡𝓐𝓘𝓓 <𝓬𝓸𝓾𝓷𝓽> <𝓾𝓼𝓮𝓻𝓷𝓪𝓶𝓮>
  2) {hl}𝓢𝓡𝓐𝓘𝓓 <𝓬𝓸𝓾𝓷𝓽> <𝓻𝓮𝓹𝓵𝔂 𝓽𝓸 𝓾𝓼𝓮𝓻>

𝓒𝓡𝓐𝓘𝓓: **𝓐𝓑𝓒𝓓 𝓡𝓐𝓘𝓓 𝓞𝓝 𝓤𝓢𝓔𝓡**
  1) {hl}𝓒𝓡𝓐𝓘𝓓 <𝓬𝓸𝓾𝓷𝓽> <𝓾𝓼𝓮𝓻𝓷𝓪𝓶𝓮>
  2) {hl}𝓒𝓡𝓐𝓘𝓓 <𝓬𝓸𝓾𝓷𝓽> <𝓻𝓮𝓹𝓵𝔂 𝓽𝓸 𝓾𝓼𝓮𝓻>


**@rasedidstore**
"""

spam_msg = f"""
**» 𝓢𝓟𝓐𝓜 𝓒𝓞𝓜𝓜𝓐𝓝𝓓𝓢:**

𝓢𝓟𝓐𝓜: **𝓢𝓟𝓐𝓜𝓢 𝓐 𝓜𝓔𝓢𝓢𝓐𝓖𝓔**
  1) {hl}𝓢𝓟𝓐𝓜 <𝓬𝓸𝓾𝓷𝓽> <𝓶𝓮𝓼𝓼𝓪𝓰𝓮 𝓽𝓸 𝓼𝓹𝓪𝓶>
  2) {hl}𝓢𝓟𝓐𝓜 <𝓬𝓸𝓾𝓷𝓽> <𝓻𝓮𝓹𝓵𝔂𝓲𝓷𝓰 𝓪𝓷𝔂 𝓶𝓮𝓼𝓼𝓪𝓰𝓮>

𝓟𝓞𝓡𝓝𝓢𝓟𝓐𝓜: **𝓟𝓞𝓡𝓜𝓞𝓖𝓡𝓐𝓟𝓗𝓨 𝓢𝓟𝓐𝓜**
  1) {hl}𝓟𝓢𝓟𝓐𝓜 <𝓬𝓸𝓾𝓷𝓽>

𝓗𝓐𝓝𝓖: **𝓢𝓟𝓐𝓜𝓢 𝓗𝓐𝓝𝓖𝓘𝓝𝓖 𝓜𝓔𝓢𝓢𝓐𝓖𝓔 𝓕𝓞𝓡 𝓖𝓘𝓥𝓔𝓝 𝓒𝓞𝓤𝓝𝓣𝓔𝓡**
  1) {hl}𝓗𝓐𝓝𝓖 <𝓬𝓸𝓾𝓷𝓽>


**@rasedidstore**
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
                Button.inline("• 𝓢𝓟𝓐𝓜 •", data="spam"),
                Button.inline("• 𝓡𝓐𝓘𝓓 •", data="raid")
              ],
              [
                Button.inline("• 𝓔𝓧𝓣𝓡𝓐 •", data="extra")
              ],
              [
                Button.url("• 𝓖𝓡𝓞𝓤𝓟 •", "https://t.me/FriendCastel"),
                Button.url("• 𝓢𝓤𝓟𝓟𝓞𝓡𝓣 •", "https://t.me/UNI_INDIA_0008")
              ]
            ]
          )
    else:
        await event.answer("𝓜𝓐𝓚𝓔 𝓨𝓞𝓤𝓡 𝓞𝓦𝓝 𝓓𝓔𝓥𝓘𝓛 𝓧 𝓑𝓞𝓣𝓢 !! @rasedidstore, cache_time=0, alert=True)


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
              buttons=[[Button.inline("< 𝓑𝓪𝓬𝓴", data="𝓱𝓮𝓵𝓹_𝓫𝓪𝓬𝓴"),],],
              ) 
    else:
        await event.answer("𝓜𝓐𝓚𝓔 𝓨𝓞𝓤𝓡 𝓞𝓦𝓝 𝓓𝓔𝓥𝓘𝓛 𝓧 𝓑𝓞𝓣𝓢 !! @rasedidstore", cache_time=0, alert=True)


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
            buttons=[[Button.inline("< 𝓑𝓪𝓬𝓴", data="𝓱𝓮𝓵𝓹_𝓫𝓪𝓬𝓴"),],],
          )
    else:
        await event.answer("𝓜𝓐𝓚𝓔 𝓨𝓞𝓤𝓡 𝓞𝓦𝓝 𝓓𝓔𝓥𝓘𝓛 𝓧 𝓑𝓞𝓣𝓢 !! @rasedidstore", cache_time=0, alert=True)


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
            buttons=[[Button.inline("< 𝓑𝓪𝓬𝓴", data="𝓱𝓮𝓵𝓹_𝓫𝓪𝓬𝓴"),],],
            )
    else:
        await event.answer("𝓜𝓐𝓚𝓔 𝓨𝓞𝓤𝓡 𝓞𝓦𝓝 𝓓𝓔𝓥𝓘𝓛 𝓧 𝓑𝓞𝓣𝓢 !! @rasedidstore", cache_time=0, alert=True)
