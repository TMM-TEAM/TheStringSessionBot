from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import SUPPORT_CHAT, OWNER_ID


keyboard = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text="ᴀᴅᴅ ʜᴀʀʟᴇʏ ᴍᴜꜱɪᴄ ɪɴ ʏᴏᴜʀ ꜱᴜᴘᴇʀ ɢʀᴏᴜᴘ 📈", url=f"https://t.me/Harley_X_Robot")],
        [
            InlineKeyboardButton(text="Dᴇᴠᴇʟᴏᴘᴇʀ ⛵", url=f"https://t.me/ITS_HELLL_BOYYY"),
            InlineKeyboardButton(
                text="Uᴘᴅᴀᴛᴇꜱ 🎊", url=f"https://t.me/GJ516_DISCUSS_GROUP"
            ),
        ],
    ]
)

keyboard2 = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text="💖 Gᴇɴᴇʀᴀᴛᴇ Sᴇssɪᴏɴ 💖", callback_data="gensession")],
        
    ]
)

gen_key = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="Pʏʀᴏɢʀᴀᴍ v1 ", callback_data="pyrogram1"),
            InlineKeyboardButton(text="Pʏʀᴏɢʀᴀᴍ v2", callback_data="pyrogram"),
        ],
        [InlineKeyboardButton(text="Tᴇʟᴇᴛʜᴏɴ", callback_data="telethon")],
    ]
)

retry_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="Tʀʏ Aɢᴀɪɴ 🙄", callback_data="gensession")]]
)
