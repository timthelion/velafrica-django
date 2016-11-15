# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-15 09:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public_site', '0006_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=255, unique=True, verbose_name=b'Key')),
                ('value', models.TextField(verbose_name=b'Value')),
                ('language', models.CharField(max_length=2, verbose_name=b'Sprache')),
            ],
            options={
                'verbose_name': 'Inhalt',
                'verbose_name_plural': 'Inhalte',
            },
        ),
    ]
