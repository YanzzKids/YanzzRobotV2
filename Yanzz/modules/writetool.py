import requests
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.ext import CallbackContext
from telegram.ext.dispatcher import run_async

from Hikari import BOT_NAME, BOT_USERNAME, dispatcher
from Hikari.modules.disable import DisableAbleCommandHandler


@run_async
def handwrite(update: Update, context: CallbackContext):
    message = update.effective_message
    if message.reply_to_message:
        text = message.reply_to_message.text
    else:
        text = update.effective_message.text.split(None, 1)[1]
    m = message.reply_text("Menulis teks...")
    req = requests.get(f"https://api.sdbots.tk/write?text={text}").url
    message.reply_photo(
        photo=req,
        caption=f"""
Teks Berhasil Ditulis 🚀

✏️ **Nulis by :** [{BOT_NAME}](https://t.me/{BOT_USERNAME})
👤 **Permintaan dari :** {update.effective_user.first_name}
🔗 **telegraph  :** `{req}`""",
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("• ᴛᴇʟᴇɢʀᴀᴩʜ •", url=req),
                ],
            ]
        ),
    )
    m.delete()


__help__ = """
 Menulis teks yang diberikan pada halaman putih dengan pensil 🖊

• /nulis <text> *:* Menulis teks yang diberikan.
"""

WRITE_HANDLER = DisableAbleCommandHandler("write", handwrite)

dispatcher.add_handler(WRITE_HANDLER)

__mod_name__ = "ɴᴜʟɪs"
__command_list__ = ["nulis"]
__handlers__ = [WRITE_HANDLER]
