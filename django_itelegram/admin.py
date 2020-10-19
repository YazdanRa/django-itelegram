from django.contrib import admin

from .models import TelegramUser, TelegramUpdate


@admin.register(TelegramUser)
class Profile(admin.ModelAdmin):
    list_display = ["id", "username", "full_name", "is_bot"]
    list_display_links = ["id", "username"]
    list_filter = ["is_bot", "date_met", "language_code"]
    search_fields = ["username", "first_name", "last_name", "bots"]


@admin.register(TelegramUpdate)
class UpdateAdmin(admin.ModelAdmin):
    list_display = ["update_id", "bot"]
    list_display_links = ["update_id"]
    list_filter = ["bot"]
    search_fields = ["update_id", "bot", "message"]
