from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import SUPPORT_CHAT, OWNER_ID


keyboard = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text="how to Use Me", callback_data="help")],
        [
            InlineKeyboardButton(text="Owner", user_id=config.QWNER_ID),
            InlineKeyboardButton(
                text="sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/GJ516_DISCUSS_GROUP"
            ),
        ],
    ]
)

keyboard2 = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text="ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ", callback_data="gensession")],
        
    ]
)

gen_key = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="ᴩʏʀᴏɢʀᴀᴍ v1", callback_data="pyrogram1"),
            InlineKeyboardButton(text="ᴩʏʀᴏɢʀᴀᴍ v2", callback_data="pyrogram"),
        ],
        [InlineKeyboardButton(text="ᴛᴇʟᴇᴛʜᴏɴ", callback_data="telethon")],
    ]
)

retry_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="ᴛʀʏ ᴀɢᴀɪɴ", callback_data="gensession")]]
)
