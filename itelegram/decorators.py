from functools import wraps

from django.conf import settings
from django.contrib.auth.models import User
from django_itelegram.defaults import telegram_not_logged_in_text, telegram_permission_denied_text, telegram_parse_mode
from telegram import Update
from telegram.ext import CallbackContext, DispatcherHandlerStop


def user_passes_test(test_func):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(update: Update, context: CallbackContext, *args, **kwargs):
            chat_id = update.message.from_user.id
            try:
                user = User.objects.get(telegram_id=chat_id)
            except User.DoesNotExist:
                context.bot.send_message(
                    chat_id=chat_id,
                    text=getattr(settings, "TELEGRAM_NOT_LOGGED_IN_TEXT", telegram_not_logged_in_text),
                    parse_mode=getattr(settings, "TELEGRAM_PARSE_MODE", telegram_parse_mode),
                )
                raise DispatcherHandlerStop
            if test_func(user):
                return view_func(update, context, *args, **kwargs)
            context.bot.send_message(
                chat_id=chat_id,
                text=getattr(settings, "TELEGRAM_PERMISSION_DENIED_TEXT", telegram_permission_denied_text),
                parse_mode=getattr(settings, "TELEGRAM_PARSE_MODE", telegram_parse_mode),
            )
            raise DispatcherHandlerStop

        return _wrapped_view

    return decorator


def telegram_perm(perm):
    def check_perms(user):
        if isinstance(perm, str):
            perms = (perm,)
        else:
            perms = perm
        # Check if the user has the permission
        if user.has_perms(perms):
            return True
        # User has not permissions
        return False

    return user_passes_test(check_perms)