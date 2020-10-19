import logging

from SampleProject.bot.handlers import start
from django_itelegram import GlobalHandler
from django_itelegram.apps import DjangoTelegramBot
from django_itelegram.services import process_update, process_error

# Logging
logger = logging.getLogger(__name__)


# Process all the updates from telegram
def telegram_process_update(update, context):
    # Here add your optional name for your bot
    # This is an optional feature! track and store all the updates and users in database
    process_update(update, "MyOptionalBotName")


UPDATE_PROCESS_HANDLER = GlobalHandler(telegram_process_update)


def main():
    logger.info("Loading handlers for telegram bot")

    # Default dispatcher (this is related to the first bot in settings.TELEGRAM_BOT_TOKENS)
    bot = DjangoTelegramBot.dispatcher
    # To get Dispatcher related to a specific bot
    #
    # bot = DjangoTelegramBot.getDispatcher('BOT_n_token')     # get by bot token
    # bot = DjangoTelegramBot.getDispatcher('BOT_n_username')  # get by bot username
    # bot = DjangoTelegramBot.getDispatcher('BOT_ID)           # get by bot optional ID in settings configuration

    # Prepare handlers
    handlers = [
        (UPDATE_PROCESS_HANDLER, 0),
        (start.HANDLER, 1),
        # Other handlers comes here
        # (HANDLER, GROUP)
    ]
    # Add Handlers to bot
    for handler in handlers:
        bot.add_handler(*handler)

    # Log all errors
    bot.add_error_handler(process_error)
