# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-28 09:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0016_auto_20160621_1025'),
        ('velafrica_sud', '0018_auto_20160620_1359'),
    ]

    operations = [
        migrations.AddField(
            model_name='container',
            name='warehouse_from',
            field=models.ForeignKey(blank=True, help_text=b'Lager wo die Velos verladen wurden', null=True, on_delete=django.db.models.deletion.CASCADE, to='stock.Warehouse', verbose_name=b'Export Lager'),
        ),
        migrations.AddField(
            model_name='historicalcontainer',
            name='warehouse_from',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='stock.Warehouse'),
        ),
    ]
