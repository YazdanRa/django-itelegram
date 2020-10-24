from django.conf import settings
from django.conf.urls import url

from . import views

webhook_base = settings.DJANGO_TELEGRAMBOT.get("WEBHOOK_PREFIX", "/")
# Fix starter /
if webhook_base.startswith("/"):
    webhook_base = webhook_base[1:]
# Fix end /
if not webhook_base.endswith("/"):
    webhook_base += "/"

urlpatterns = [
    url(r"admin/django-itelegram", views.home, name="itelegram"),
    url(r"{}(?P<bot_token>.+?)".format(webhook_base), views.webhook, name="webhook"),
]
