import logging

from telegram import Update
from telegram.ext import (
    Updater,
    CallbackContext,
    MessageHandler,
)
import sys

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

BAN_LIST = [
    'HV Cursos',
    'Hadassa',
    'Hadassa Cursos',
]

def handle_blacklist(update: Update, context: CallbackContext) -> None:
    bot = context.bot
    msg = update.message
    for new_member in msg.new_chat_members:
        if new_member.first_name in BAN_LIST or new_member.last_name in BAN_LIST or new_member.username in BAN_LIST:
            msg.reply_text(f"{new_member.first_name}, you are not welcome here.")
            bot.banChatMember(chat_id=msg.chat.id, user_id=new_member.id)
            msg.reply_text("Bye bye.")


def run_bot(bot_token) -> None:
    updater = Updater(bot_token)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(MessageHandler(None, handle_blacklist))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    assert len(sys.argv) == 2, "Please, provide the bot token to run."
    run_bot(sys.argv[1])
