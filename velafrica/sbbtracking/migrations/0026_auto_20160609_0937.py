# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-09 07:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sbbtracking', '0025_auto_20160601_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicaltrackingeventtype',
            name='show_partner_info',
            field=models.BooleanField(default=False, help_text=b'Zeige Partnerinfo an wenn vorhanden (Wird aus hinterlegtem Container ausgelesen).'),
        ),
        migrations.AddField(
            model_name='trackingeventtype',
            name='show_partner_info',
            field=models.BooleanField(default=False, help_text=b'Zeige Partnerinfo an wenn vorhanden (Wird aus hinterlegtem Container ausgelesen).'),
        ),
    ]
