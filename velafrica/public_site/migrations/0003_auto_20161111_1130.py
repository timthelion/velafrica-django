# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-11 10:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public_site', '0002_walkthroughrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='walkthroughrequest',
            name='collected_before',
            field=models.BooleanField(default=False, verbose_name=b'Bereits f\xc3\xbcr Velafrica gesammelt'),
        ),
        migrations.AddField(
            model_name='walkthroughrequest',
            name='collected_before_note',
            field=models.TextField(blank=True, verbose_name=b'Wann und wo'),
        ),
        migrations.AlterField(
            model_name='walkthroughrequest',
            name='organizer_type',
            field=models.IntegerField(choices=[(1, b'Verein'), (2, b'Firma'), (3, b'Gemeinde'), (4, b'Kirchgemeinde'), (5, b'Schule'), (6, b'Liegenschaftsverwaltung'), (7, b'Privatperson'), (8, b'Andere')], default=1, verbose_name=b'Veranstalter'),
        ),
    ]