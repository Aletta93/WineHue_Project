# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-26 16:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Wine', '0007_auto_20161026_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='wine_detail',
            name='picture',
            field=models.ImageField(default='not_found.png', upload_to=''),
        ),
    ]
