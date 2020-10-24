from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from .models import TelegramUser, TelegramUpdate


def linkify(field_name):
    """
    Converts a foreign key value into clickable links.
    """

    def _linkify(obj):
        linked_obj = getattr(obj, field_name)
        if linked_obj is None:
            return "Disconnected!"
        app_label = linked_obj._meta.app_label
        model_name = linked_obj._meta.model_name
        view_name = f"admin:{app_label}_{model_name}_change"
        link_url = reverse(view_name, args=[linked_obj.pk])
        return format_html('<a href="{}">{}</a>', link_url, linked_obj)

    _linkify.short_description = field_name  # Sets column name
    return _linkify


@admin.register(TelegramUser)
class Profile(admin.ModelAdmin):
    list_display = ["id", "username", "full_name", "is_bot", linkify("site_user")]
    list_display_links = ["id", "username"]
    list_filter = ["is_bot", "language_code", "date_met", "last_seen", "bots"]
    readonly_fields = ["id", "bots", "username", "first_name", "last_name", "date_met", "last_seen"]
    search_fields = [
        # Telegram fields
        "username",
        "first_name",
        "last_name",
        "bots",
        # User fields
        "site_user__first_name",
        "site_user__last_name",
        "site_user__{}".format(User.USERNAME_FIELD),
    ]
    fieldsets = (
        (
            _("personal information"),
            {
                "fields": (
                    "username",
                    ("first_name", "last_name"),
                    "phone_number",
                )
            },
        ),
        (_("Telegram data"), {"fields": ("is_bot", "language_code", "bots")}),
        (
            _("Last updates"),
            {"fields": ("date_met", "last_login")},
        ),
    )


@admin.register(TelegramUpdate)
class UpdateAdmin(admin.ModelAdmin):
    list_display = ["update_id", "bot"]
    list_display_links = ["update_id"]
    list_filter = ["bot"]
    search_fields = ["update_id", "bot", "message"]
