# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-12 15:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('public_site', '0020_event_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventDateTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name=b'Datum')),
                ('time_start', models.CharField(max_length=255, verbose_name=b'Von')),
                ('time_end', models.CharField(max_length=255, verbose_name=b'Bis')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='datetimes', to='public_site.Event')),
            ],
        ),
    ]