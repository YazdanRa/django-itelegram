from telegram.ext import Handler


class GlobalHandler(Handler):
    def check_update(self, update):
        return True


default_app_config = "itelegram.apps.DjangoTelegramBot"
