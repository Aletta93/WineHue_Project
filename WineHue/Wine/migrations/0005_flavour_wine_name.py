# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-28 18:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Wine', '0004_remove_wine_detail_flavours'),
    ]

    operations = [
        migrations.AddField(
            model_name='flavour',
            name='wine_name',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Wine.Wine_Detail'),
            preserve_default=False,
        ),
    ]