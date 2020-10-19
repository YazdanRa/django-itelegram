from django.contrib.postgres.fields import JSONField, ArrayField
from django.db import models


class TelegramUser(models.Model):
    id = models.BigIntegerField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    is_bot = models.BooleanField(default=False)
    language_code = models.CharField(max_length=8, null=True, blank=True)
    bots = ArrayField(models.CharField(max_length=32))
    date_met = models.DateTimeField(auto_now_add=True)
    last_seen = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "{} {} (@{})".format(self.first_name, self.last_name, self.username)


class TelegramUpdate(models.Model):
    update_id = models.CharField(max_length=128)
    bot = models.CharField(max_length=32)
    message = JSONField(null=True, blank=True)
    edited_message = JSONField(null=True, blank=True)
    channel_post = JSONField(null=True, blank=True)
    edited_channel_post = JSONField(null=True, blank=True)
    inline_query = JSONField(null=True, blank=True)
    chosen_inline_result = JSONField(null=True, blank=True)
    callback_query = JSONField(null=True, blank=True)
