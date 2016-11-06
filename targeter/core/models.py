from django.db import models

from core import common_models as cm
from core import behaviors as bh


class User(cm.Common):
    """
    Пользователь Инстаграма
    """
    user_id = models.BigIntegerField(
        verbose_name='ID пользователя',
        unique=True
    )
    username = models.CharField(
        max_length=200,
        verbose_name='Никнейм',
        unique=True
    )
    access_token = models.CharField(
        max_length=200,
        verbose_name='Токен'
    )

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        ordering = ['-created']

    def __str__(self):
        return str(self.user_id)


class Tag(cm.Common):
    """
    Поисковые хэштэги Пользователя
    """
    user = models.ForeignKey(
        'core.User',
        verbose_name='Пользователь',
        related_name='tag_list'
    )
    text = models.CharField(
        max_length=30,
        verbose_name='Текст'
    )

    class Meta:
        verbose_name = 'хэштэг'
        verbose_name_plural = 'хэштэги'

    def __str__(self):
        return self.text