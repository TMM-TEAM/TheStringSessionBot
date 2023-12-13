from pyrogram import filters
from pyrogram.types import Message

from StringGen import Anony
from StringGen.utils import add_served_user, keyboard, keyboard2


@Anony.on_message(filters.command("start") & filters.private & filters.incoming)
async def f_start(_, message: Message):
    await message.reply_text(
        text=f"ʜᴇʏ {message.from_user.first_name},\n\n๏ ᴛʜɪs ɪs {Anony.mention},\nᴘʟᴇᴀꜱᴇ ᴄʜᴏᴏꜱᴇ ᴛʜᴇ ᴘʏᴛʜᴏɴ ʟɪʙʀᴀʀʏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ꜰᴏʀ. ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ ᴩʏʀᴏɢʀᴀᴍ.",
        reply_markup=keyboard,
        disable_web_page_preview=True,
    )
    await add_served_user(message.from_user.id)

#help

@Anony.on_message(filters.command("help") & filters.private & filters.incoming)
async def f_help(_, message: Message):
    await message.reply_text(
        text=f"""
        ✅ 𝗦𝘁𝗲𝗽𝘀 𝘁𝗼 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲 𝗦𝗲𝘀𝘀𝗶𝗼𝗻 𝗦𝘁𝗿𝗶𝗻𝗴

 ▪️ ꜱᴇꜱꜱɪᴏɴ ꜱᴛʀɪɴɢ ɪꜱ ɴᴇᴇᴅ ꜰᴏʀ ᴜꜱᴇʀʙᴏᴛꜱ, ɪ ᴄᴀɴ ɢᴇɴᴇʀᴀᴛᴇ ꜱᴇꜱꜱɪᴏɴ ꜱᴛʀɪɴɢ ꜰᴏʀ ʙᴏᴛʜ ᴘʏʀᴏɢʀᴀᴍ & ᴛᴇʟᴇᴛʜᴏɴ.

 ▪️ ꜱᴇɴᴅ /start ᴛᴏ ꜱᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ꜱᴇꜱꜱɪᴏɴ ꜱᴛʀɪɴɢ.

1. ɪ ɴᴇᴇᴅꜱ API_ID, API_HASH (ʙᴏᴛʜ ᴄᴀɴ ʙᴇ ɢᴇᴛ ꜰʀᴏᴍ my.telegram.org), ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ ᴀɴᴅ ᴏɴᴇ ᴛɪᴍᴇ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ᴄᴏᴅᴇ ᴡʜɪᴄʜ ᴡɪʟʟ ʙᴇ ꜱᴇɴᴛ ᴛᴏ ʏᴏᴜʀ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ.

2. ʏᴏᴜ ʜᴀᴠᴇ ᴛᴏ ᴘᴜᴛ ᴏᴛᴘ ɪɴ 1 2 3 4 5 6 ᴛʜɪꜱ ꜰᴏʀᴍᴀᴛ.

3. ɪꜰ ᴛꜰᴀ ᴇɴᴀʙʟᴇᴅ ɪɴ ʏᴏᴜʀ ᴀᴄᴄᴏᴜɴᴛ, ʙᴏᴛ ᴡɪʟʟ ᴀʟꜱᴏ ᴀꜱᴋ ᴛʜᴀᴛ ꜰᴏʀ ɢᴇɴᴇʀᴀᴛɪɴɢ ꜱᴇꜱꜱɪᴏɴ ꜱᴛʀɪɴɢ ᴘᴜʀᴘᴏꜱᴇ ᴏɴʟʏ.      """,
        reply_markup=keyboard2,
        disable_web_page_preview=True,
    )
    await add_served_user(message.from_user.id)
