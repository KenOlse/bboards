from django.db import models
from django.contrib.auth.models import AbstractUser


class AdvUser(AbstractUser):
    """docstring for AdvUser"""

    is_activated = models.BooleanField(default=True,
                                       db_index=True, verbose_name='Актівацію пройдено')
    send_messages = models.BooleanField(default=True,
                                        verbose_name='Присилати сповіщення щодо коментарів')

    class Meta(AbstractUser.Meta):
        pass
