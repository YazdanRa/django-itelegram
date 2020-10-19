from telegram.ext import Handler


class GlobalHandler(Handler):
    def check_update(self, update):
        return True


__version__ = "1.0.0"
default_app_config = "django_itelegram.apps.DjangoTelegramBot"
