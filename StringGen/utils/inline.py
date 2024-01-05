from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import SUPPORT_CHAT, OWNER_ID


keyboard = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text=" 會| ˹ᴀᴅᴅ ᴋʀɪᴛɪᴋᴀ ᴍᴜꜱɪᴄ ʙᴏᴛ˼ |會", url=f"https://t.me/KRITIKAMUSICBOT")],
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
