# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-17 11:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public_site', '0012_award_text'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Award',
            new_name='References',
        ),
        migrations.AlterModelOptions(
            name='references',
            options={'verbose_name': 'Botschafter', 'verbose_name_plural': 'Botschafter'},
        ),
    ]