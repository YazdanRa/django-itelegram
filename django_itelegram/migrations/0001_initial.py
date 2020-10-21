import django.contrib.postgres.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="TelegramUpdate",
            options={
                "verbose_name": "Telegram Update",
                "verbose_name_plural": "Telegram Updates",
            },
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "update_id",
                    models.CharField(
                        verbose_name="Telegram Update ID",
                        max_length=128,
                        help_text="This is a unique ID for each Update from Telegram",
                    ),
                ),
                (
                    "bot",
                    models.CharField(
                        verbose_name="Telegram bot",
                        max_length=32,
                        help_text="Displays the bot which has participated is in this update.",
                    ),
                ),
                (
                    "message",
                    django.contrib.postgres.fields.jsonb.JSONField(
                        verbose_name="Telegram Update message",
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "edited_message",
                    django.contrib.postgres.fields.jsonb.JSONField(
                        verbose_name="Telegram Update edited message",
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "channel_post",
                    django.contrib.postgres.fields.jsonb.JSONField(
                        verbose_name="Telegram Update channel post",
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "edited_channel_post",
                    django.contrib.postgres.fields.jsonb.JSONField(
                        verbose_name="Telegram Update edited channel post",
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "inline_query",
                    django.contrib.postgres.fields.jsonb.JSONField(
                        verbose_name="Telegram Update inline query", null=True, blank=True
                    ),
                ),
                (
                    "chosen_inline_result",
                    django.contrib.postgres.fields.jsonb.JSONField(
                        verbose_name="Telegram Update chosen inline result",
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "callback_query",
                    django.contrib.postgres.fields.jsonb.JSONField(
                        verbose_name="Telegram Update callback query",
                        null=True,
                        blank=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TelegramUser",
            options={
                "verbose_name": "Telegram User",
                "verbose_name_plural": "Telegram Users",
            },
            fields=[
                (
                    "id",
                    models.BigIntegerField(
                        verbose_name="Telegram User ID",
                        primary_key=True,
                        serialize=False,
                        help_text="Telegram ID is a unique ID for each user which is help us tp identify users.",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        verbose_name="Telegram User First name",
                        max_length=255,
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        verbose_name="Telegram User Last name",
                        max_length=255,
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        verbose_name="Telegram User Username",
                        max_length=255,
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "is_bot",
                    models.BooleanField(
                        verbose_name="Telegram User IsBot",
                        default=False,
                        help_text="Designates whether the account is a telegram bot or a human user.",
                    ),
                ),
                (
                    "language_code",
                    models.CharField(
                        verbose_name="Telegram User Language code",
                        max_length=8,
                        null=True,
                        blank=True,
                    ),
                ),
                (
                    "bots",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(
                            verbose_name="Telegram bot",
                            max_length=32,
                            help_text="Displays the bots which have been interacted with this user.",
                        ),
                        size=None,
                    ),
                ),
                ("date_met", models.DateTimeField(auto_now_add=True)),
                ("last_seen", models.DateTimeField(blank=True, null=True)),
                (
                    "site_user",
                    models.OneToOneField(
                        verbose_name="Connected Site User",
                        on_delete=django.db.models.deletion.SET_NULL,
                        blank=True,
                        null=True,
                        related_name="telegram_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
