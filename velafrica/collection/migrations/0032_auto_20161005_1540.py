# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-05 13:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0031_auto_20161005_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dropoff',
            name='temp_end',
            field=models.DateField(blank=True, null=True, verbose_name=b'Tempor\xc3\xa4r Ende'),
        ),
        migrations.AlterField(
            model_name='dropoff',
            name='temp_start',
            field=models.DateField(blank=True, null=True, verbose_name=b'Tempor\xc3\xa4r Start'),
        ),
    ]
