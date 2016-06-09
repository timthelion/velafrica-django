# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-01 13:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('velafrica_sud', '0011_auto_20160601_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalpartnersud',
            name='area',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='historicalpartnersud',
            name='legalform',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Organisationsform'),
        ),
        migrations.AlterField(
            model_name='historicalpartnersud',
            name='org_type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='historicalpartnersud',
            name='street',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='partnersud',
            name='area',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='partnersud',
            name='legalform',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Organisationsform'),
        ),
        migrations.AlterField(
            model_name='partnersud',
            name='org_type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='partnersud',
            name='street',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]