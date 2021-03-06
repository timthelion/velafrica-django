# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-26 22:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0003_auto_20181019_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='amount',
            field=models.IntegerField(verbose_name='Anzahl Velos'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='confirmed',
            field=models.BooleanField(default=False, verbose_name='Visum Werkstattchef'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Datum'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='note',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Bemerkungen'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='organisation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organisation.Organisation', verbose_name='Verarbeitsungsort'),
        ),
        migrations.AlterField(
            model_name='historicalentry',
            name='amount',
            field=models.IntegerField(verbose_name='Anzahl Velos'),
        ),
        migrations.AlterField(
            model_name='historicalentry',
            name='confirmed',
            field=models.BooleanField(default=False, verbose_name='Visum Werkstattchef'),
        ),
        migrations.AlterField(
            model_name='historicalentry',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Datum'),
        ),
        migrations.AlterField(
            model_name='historicalentry',
            name='history_type',
            field=models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1),
        ),
        migrations.AlterField(
            model_name='historicalentry',
            name='note',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Bemerkungen'),
        ),
        migrations.AlterField(
            model_name='historicalentry',
            name='organisation',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='organisation.Organisation', verbose_name='Verarbeitsungsort'),
        ),
    ]
