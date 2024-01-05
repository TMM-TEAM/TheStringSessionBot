from pyrogram import filters
from pyrogram.types import Message

from StringGen import Anony
from StringGen.utils import add_served_user, keyboard, keyboard2


@Anony.on_message(filters.command("start") & filters.private & filters.incoming)
async def f_start(_, message: Message):
    await message.reply_photo(photo="https://telegra.ph/file/7fc57533c40ff57d070c3.jpg", caption=f" ʜᴇʏ {message.from_user.first_name},\n\n๏ ᴛʜɪs ɪs {Anony.mention},\nʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴍᴇ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴘʏʀᴏɢʀᴀᴍ (ᴇᴠᴇɴ ᴠᴇʀꜱɪᴏɴ 2) ᴀɴᴅ ᴛᴇʟᴇᴛʜᴏɴ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ. \n\nᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ ᴩʏʀᴏɢʀᴀᴍ.\n\n๏ ᴄᴏᴍᴍᴀɴᴅꜱ ꜰᴇᴀᴛᴜʀᴇs ✨\n────────────────────\n\n➲ /start : ꜱᴛᴀʀᴛꜱ ᴍᴇ | ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ᴍᴇ ʏᴏᴜ'ᴠᴇ ᴀʟʀᴇᴀᴅʏ ᴅᴏɴᴇ ɪᴛ.\n➲ /help  : ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅꜱ ɢᴇɴᴇʀᴀᴛᴇ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ.\n──────────────────── ",
        reply_markup=keyboard,
        disable_web_page_preview=True,
    )
    await add_served_user(message.from_user.id)

#help

@Anony.on_message(filters.command("help") & filters.private & filters.incoming)
async def f_help(_, message: Message):
    await message.reply_text(
        text=f"ʜᴇʏ {message.from_user.first_name},\n\n<b> ᴜꜱᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴꜱ ᴛᴏ ʟᴇᴀʀɴ ᴍᴏʀᴇ ! </b>",
        reply_markup=keyboard2,
        disable_web_page_preview=True,
    )
    await add_served_user(message.from_user.id)
