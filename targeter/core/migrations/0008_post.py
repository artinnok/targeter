# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-06 14:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20161106_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Время и дата создания')),
                ('post_id', models.BigIntegerField(verbose_name='ID поста')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_list', to='core.User', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'пост',
                'verbose_name_plural': 'посты',
            },
        ),
    ]
