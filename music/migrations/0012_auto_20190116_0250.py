# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-01-15 21:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0011_auto_20190108_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_title',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='title',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]