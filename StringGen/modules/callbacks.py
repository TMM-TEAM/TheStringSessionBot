from pyrogram import filters
from pyrogram.types import CallbackQuery

from StringGen import Anony
from StringGen.utils import gen_key, keyboard2
from StringGen.modules.gen import gen_session


@Anony.on_callback_query(
    filters.regex(pattern=r"^(gensession|pyrogram|pyrogram1|telethon)$")
)
async def _callbacks(_, cq: CallbackQuery):
    user = await bot.get_me()
    # user_id = cq.from_user.id
    mention = user.mention
    query = cq.data.lower()
    if query.startswith("help"):
        if query == 'help':
            chat_id = cq.from_user.id
            message_id = cq.message.id
            await cq.edit_message_text(
                chat_id=chat_id,
                message_id=message_id,
                text="ʜᴇʏ {cq.from_user.mention},\n\n<b> ᴜꜱᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴꜱ ᴛᴏ ʟᴇᴀʀɴ ᴍᴏʀᴇ ! </b>",
                reply_markup=keyboard2,
            )
    elif query == "gensession":
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



