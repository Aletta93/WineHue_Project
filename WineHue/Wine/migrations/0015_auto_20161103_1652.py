# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-03 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Wine', '0014_flavour_flavour_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flavour',
            name='flavour_picture',
        ),
        migrations.AddField(
            model_name='wine_detail',
            name='flavour_picture',
            field=models.ImageField(default='not_found.png', upload_to='flavour_images'),
            preserve_default=False,
        ),
    ]