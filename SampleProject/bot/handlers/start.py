from telegram import Update
from telegram.ext import CommandHandler, CallbackContext, ConversationHandler


def say_hello(update: Update, context: CallbackContext):
    context.user_data.clear()
    chat_id = update.message.from_user.id

    context.bot.send_message(
        chat_id=chat_id,
        text="Hello *{}*!".format(update.message.from_user.first_name),
        parse_mode="Markdown",
    )

    return ConversationHandler.END


HANDLER = CommandHandler("start", say_hello)
