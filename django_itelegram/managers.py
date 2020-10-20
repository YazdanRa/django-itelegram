from datetime import datetime

from django.db import models


class TelegramUserManager(models.Manager):
    """Custom Telegram User manager"""

    def get_recent_users(self, from_date: datetime):
        """
        The last users who have interaction with us
        :return QuerySet
        """
        recent_users = self.filter(date_met__gte=from_date)
        return recent_users
