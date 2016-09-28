# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-28 16:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cultivar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cultivar', models.CharField(choices=[('Sauvignon Blanc', 'Sauvignon Blanc'), ('Chardonnay', 'Chardonnay'), ('Cabernet Sauvignon', 'Cabernet Sauvignon'), ('Shiraz', 'Shiraz'), ('Merlot', 'Merlot'), ('Pinot Noir', 'Pinot Noir')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Flavours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flavour_name', models.CharField(max_length=30)),
                ('flavour_strength', models.IntegerField(choices=[(0, 'None'), (1, 'Barely Noticeable'), (2, 'Somewhat Noticeable'), (3, 'Very Noticeable'), (4, 'Dominant'), (5, 'Overpowering')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Wine_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('vineyard', models.CharField(max_length=30)),
                ('colour', models.CharField(choices=[('White', 'White'), ('Red', 'Red'), ('Rose', 'Rose')], max_length=5)),
            ],
        ),
        migrations.AddField(
            model_name='flavours',
            name='wine_name',
            field=models.ManyToManyField(to='Wine.Wine_Details'),
        ),
        migrations.AddField(
            model_name='cultivar',
            name='wine_name',
            field=models.ManyToManyField(to='Wine.Wine_Details'),
        ),
    ]