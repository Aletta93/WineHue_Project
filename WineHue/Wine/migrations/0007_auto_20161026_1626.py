# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-26 16:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Wine', '0006_auto_20160928_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='wine_detail',
            name='pic_name',
            field=models.CharField(default='not_found.png', max_length=30),
        ),
        migrations.AlterField(
            model_name='cultivar',
            name='cultivar',
            field=models.CharField(choices=[('Sauvignon Blanc', 'Sauvignon Blanc'), ('Chardonnay', 'Chardonnay'), ('Chenin Blanc', 'Chenin Blanc'), ('Cabernet Sauvignon', 'Cabernet Sauvignon'), ('Shiraz', 'Shiraz'), ('Merlot', 'Merlot'), ('Pinot Noir', 'Pinot Noir')], max_length=30),
        ),
    ]
