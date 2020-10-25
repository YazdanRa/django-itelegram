from django.conf import settings
from django.urls import path

from . import views

webhook_base: str = settings.DJANGO_TELEGRAMBOT.get("WEBHOOK_PREFIX", "")
# Fix  /
webhook_base = webhook_base.replace("/", "")
if len(webhook_base):
    webhook_base += "/"

urlpatterns = [
    path("admin", views.admin_page, name="itelegram"),
    path("{}<str:bot_token>".format(webhook_base), views.webhook, name="webhook"),
]
