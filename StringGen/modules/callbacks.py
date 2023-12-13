from pyrogram import filters
from pyrogram.types import CallbackQuery

from StringGen import Anony
from StringGen.utils import gen_key, keyboard2
from StringGen.modules.gen import gen_session


@Anony.on_callback_query(
    filters.regex(pattern=r"^(gensession|pyrogram|pyrogram1|telethon)$")
)
async def cb_choose(_, cq: CallbackQuery):
    await cq.answer()
    query = cq.matches[0].group(1)
    if query == "gensession":
        return await cq.message.reply_text(
            text="<b>» ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ғᴏʀ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ :</b>",
            reply_markup=gen_key,
        )
    elif query.startswith("pyrogram") or query.startswith("telethon"):
        try:
            if query == "pyrogram":
                await gen_session(cq.message, cq.from_user.id)
            elif query == "pyrogram1":
                await gen_session(cq.message, cq.from_user.id, old_pyro=True)
            elif query == "telethon":
                await gen_session(cq.message, cq.from_user.id, telethon=True)
        except Exception as e:
            await cq.edit_message_text(e, disable_web_page_preview=True)


@Anony.on_callback_query(filters.regex("help"))
async def help(_, query: CallbackQuery):
    try:
        await query.answer()
    except:
        pass
    try:
        await query.edit_message_text(
            text="""✅ 𝗦𝘁𝗲𝗽𝘀 𝘁𝗼 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲 𝗦𝗲𝘀𝘀𝗶𝗼𝗻 𝗦𝘁𝗿𝗶𝗻𝗴

 ▪️ ꜱᴇꜱꜱɪᴏɴ ꜱᴛʀɪɴɢ ɪꜱ ɴᴇᴇᴅ ꜰᴏʀ ᴜꜱᴇʀʙᴏᴛꜱ, ɪ ᴄᴀɴ ɢᴇɴᴇʀᴀᴛᴇ ꜱᴇꜱꜱɪᴏɴ ꜱᴛʀɪɴɢ ꜰᴏʀ ʙᴏᴛʜ ᴘʏʀᴏɢʀᴀᴍ & ᴛᴇʟᴇᴛʜᴏɴ.

 ▪️ ꜱᴇɴᴅ /start ᴛᴏ ꜱᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ꜱᴇꜱꜱɪᴏɴ ꜱᴛʀɪɴɢ.

1. ɪ ɴᴇᴇᴅꜱ API_ID, API_HASH (ʙᴏᴛʜ ᴄᴀɴ ʙᴇ ɢᴇᴛ ꜰʀᴏᴍ my.telegram.org), ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ ᴀɴᴅ ᴏɴᴇ ᴛɪᴍᴇ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ᴄᴏᴅᴇ ᴡʜɪᴄʜ ᴡɪʟʟ ʙᴇ ꜱᴇɴᴛ ᴛᴏ ʏᴏᴜʀ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ.

2. ʏᴏᴜ ʜᴀᴠᴇ ᴛᴏ ᴘᴜᴛ ᴏᴛᴘ ɪɴ 1 2 3 4 5 6 ᴛʜɪꜱ ꜰᴏʀᴍᴀᴛ.

3. ɪꜰ ᴛꜰᴀ ᴇɴᴀʙʟᴇᴅ ɪɴ ʏᴏᴜʀ ᴀᴄᴄᴏᴜɴᴛ, ʙᴏᴛ ᴡɪʟʟ ᴀʟꜱᴏ ᴀꜱᴋ ᴛʜᴀᴛ ꜰᴏʀ ɢᴇɴᴇʀᴀᴛɪɴɢ ꜱᴇꜱꜱɪᴏɴ ꜱᴛʀɪɴɢ ᴘᴜʀᴘᴏꜱᴇ ᴏɴʟʏ."""
            ),
            reply_markup=keyboard2,
        )
    except:
        pass
