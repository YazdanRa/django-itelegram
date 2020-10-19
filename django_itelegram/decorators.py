from functools import wraps

from django.contrib.auth.models import User
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
                context.bot.send_message(chat_id, "Permission Denied!")
                raise DispatcherHandlerStop
            if test_func(user):
                return view_func(update, context, *args, **kwargs)
            context.bot.send_message(chat_id, "Permission Denied!")
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
