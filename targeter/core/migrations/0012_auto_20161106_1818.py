# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-06 15:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20161106_1810'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coordinate',
            name='created_time',
        ),
        migrations.AddField(
            model_name='post',
            name='created_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Время публикации'),
            preserve_default=False,
        ),
    ]
