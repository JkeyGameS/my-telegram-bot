from telegram.ext import Updater, CommandHandler

# Temporary imghdr patch for Python 3.13
import sys
if sys.version_info >= (3, 13):
    import mimetypes
    import types
    def what(file, h=None):
        kind = mimetypes.guess_type(file)[0]
        if kind:
            if "jpeg" in kind:
                return "jpeg"
            elif "png" in kind:
                return "png"
        return None
    sys.modules['imghdr'] = types.SimpleNamespace(what=what)

import os

TOKEN = os.getenv("BOT_TOKEN")

def start(update, context):
    update.message.reply_text("Hello! I'm alive 24/7 🚀")

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))

updater.start_polling()
updater.idle()
