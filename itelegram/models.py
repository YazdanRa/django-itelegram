from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import TelegramUserManager


class TelegramUser(models.Model):
    objects = TelegramUserManager

    id = models.BigIntegerField(
        verbose_name=_("Telegram User ID"),
        primary_key=True,
        help_text=_("Telegram ID is a unique ID for each user which is help us tp identify users."),
    )
    first_name = models.CharField(
        verbose_name=_("Telegram User First name"),
        max_length=255,
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        verbose_name=_("Telegram User Last name"),
        max_length=255,
        null=True,
        blank=True,
    )
    username = models.CharField(
        verbose_name=_("Telegram User Username"),
        max_length=255,
        null=True,
        blank=True,
    )
    is_bot = models.BooleanField(
        verbose_name=_("Telegram User IsBot"),
        default=False,
        help_text=_("Designates whether the account is a telegram bot or a human user."),
    )
    language_code = models.CharField(
        verbose_name=_("Telegram User Language code"),
        max_length=8,
        null=True,
        blank=True,
    )
    bots = ArrayField(
        models.CharField(
            verbose_name=_("Telegram bot"),
            max_length=32,
            help_text=_("Displays the bots which have been interacted with this user."),
        )
    )
    date_met = models.DateTimeField(auto_now_add=True)
    last_seen = models.DateTimeField(null=True, blank=True)

    # Optional fields
    site_user = models.OneToOneField(
        verbose_name=_("Connected Site User"),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="telegram",
        to=settings.AUTH_USER_MODEL,
    )
    phone_number = models.CharField(
        verbose_name=_("Phone number"),
        max_length=16,
        unique=True,
    )

    class Meta:
        verbose_name = _("Telegram User")
        verbose_name_plural = _("Telegram Users")

    def __str__(self):
        return "{} {} (@{})".format(self.first_name, self.last_name, self.username)

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name).strip()


class TelegramUpdate(models.Model):
    update_id = models.CharField(
        verbose_name=_("Telegram Update ID"),
        max_length=128,
        help_text=_("This is a unique ID for each Update from Telegram"),
    )
    bot = models.CharField(
        verbose_name=_("Telegram bot"),
        max_length=32,
        help_text=_("Displays the bot which has participated is in this update."),
    )
    message = models.JSONField(
        verbose_name=_("Telegram Update message"),
        null=True,
        blank=True,
    )
    edited_message = models.JSONField(
        verbose_name=_("Telegram Update edited message"),
        null=True,
        blank=True,
    )
    channel_post = models.JSONField(
        verbose_name=_("Telegram Update channel post"),
        null=True,
        blank=True,
    )
    edited_channel_post = models.JSONField(
        verbose_name=_("Telegram Update edited channel post"),
        null=True,
        blank=True,
    )
    inline_query = models.JSONField(
        verbose_name=_("Telegram Update inline query"),
        null=True,
        blank=True,
    )
    chosen_inline_result = models.JSONField(
        verbose_name=_("Telegram Update chosen inline result"),
        null=True,
        blank=True,
    )
    callback_query = models.JSONField(
        verbose_name=_("Telegram Update callback query"),
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _("Telegram Update")
        verbose_name_plural = _("Telegram Updates")

    def __str__(self):
        return "{} | {}".format(self.update_id, self.bot)
