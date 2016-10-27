# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-27 13:18
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Wine', '0010_auto_20161026_1723'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wine_detail',
            name='pic_name',
        ),
        migrations.AddField(
            model_name='wine_detail',
            name='colour_blue',
            field=models.PositiveIntegerField(default=254, validators=[django.core.validators.MaxValueValidator(254)]),
        ),
        migrations.AddField(
            model_name='wine_detail',
            name='colour_green',
            field=models.PositiveIntegerField(default=254, validators=[django.core.validators.MaxValueValidator(254)]),
        ),
        migrations.AddField(
            model_name='wine_detail',
            name='colour_red',
            field=models.PositiveIntegerField(default=254, validators=[django.core.validators.MaxValueValidator(254)]),
        ),
    ]
