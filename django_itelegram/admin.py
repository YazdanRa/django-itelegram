from django.contrib import admin

from .models import TelegramUser


@admin.register(TelegramUser)
class Profile(admin.ModelAdmin):
    list_display = ("id", "username", "full_name", "is_bot")
    list_display_links = ("id", "username")
    list_filter = ("is_bot", "date_met", "language_code")
    search_fields = ("username", "first_name", "last_name", "bots")
