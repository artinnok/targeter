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


class Post(bh.Textable, cm.Common):
    """
    Пост Пользователя
    """
    post_id = models.BigIntegerField(
        verbose_name='ID поста'
    )
    user = models.ForeignKey(
        'core.User',
        verbose_name='Пользователь',
        related_name='post_list'
    )

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'

    def __str__(self):
        return self.text


class KeyWord(cm.Common):
    """
    Ключевые слова Пользователя, по которым производится поиск
    """
    user = models.ForeignKey(
        'core.User',
        verbose_name='Пользователь',
        related_name='keyword_list'
    )
    text = models.CharField(
        max_length=30,
        verbose_name='Текст'
    )

    class Meta:
        verbose_name = 'ключевое слово'
        verbose_name_plural = 'ключевые слова'

    def __str__(self):
        return self.text


class Coordinate(cm.Common):
    """
    Координаты Пользователя, по которым производится поиск
    """
    user = models.ForeignKey(
        'core.User',
        verbose_name='Пользователь',
        related_name='coordinate_list'
    )
    lat = models.DecimalField(
        verbose_name='Широта',
        max_digits=20,
        decimal_places=14
    )
    lng = models.DecimalField(
        verbose_name='Долгота',
        max_digits=20,
        decimal_places=14
    )
    created_time = models.DateTimeField(
        verbose_name='Время публикации'
    )

    class Meta:
        verbose_name = 'координата'
        verbose_name_plural = 'координаты'

    def __str__(self):
        return 'Широта: {}, Долгота: {}'.format(self.lat, self.lng)
