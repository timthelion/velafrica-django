# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-09 14:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0005_auto_20160609_1624'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Muncipality',
            new_name='Municipality',
        ),
    ]
