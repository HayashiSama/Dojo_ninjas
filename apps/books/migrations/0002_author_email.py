# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-20 19:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='email',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
