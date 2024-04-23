from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import SUPPORT_CHAT, OWNER_ID


keyboard = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text=" 會| 丂ᴘᴏᴛɪғʏ ᴍᴜsɪᴄ |會", url=f"https://t.me/Spotify_x_music_bot")],
        [
            InlineKeyboardButton(text="𝐃ᴇᴠᴇʟᴏᴘᴇʀ ⛵", url=f"https://t.me/tmm_heroku_world"),
            InlineKeyboardButton(
                text="𝐔ᴘᴅᴀᴛᴇꜱ 🎊", url=f"https://t.me/tmm_support_chat"
            ),
        ],
    ]
)

keyboard2 = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text="⚡ 𝐆ᴇɴᴇʀᴀᴛᴇ 𝐒ᴇssɪᴏɴ ⚡", callback_data="gensession")],
        
    ]
)

gen_key = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="𝐏ʏʀᴏɢʀᴀᴍ v1 ", callback_data="pyrogram1"),
            InlineKeyboardButton(text="𝐏ʏʀᴏɢʀᴀᴍ v2", callback_data="pyrogram"),
        ],

    ]
)

retry_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="𝐓ʀʏ 𝐀ɢᴀɪɴ 🙄", callback_data="gensession")]]
)
