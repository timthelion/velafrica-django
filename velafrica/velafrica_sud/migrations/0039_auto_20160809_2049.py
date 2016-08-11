# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-09 18:49
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('velafrica_sud', '0038_delete_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalreport',
            name='currency',
            field=models.CharField(default=b'', max_length=10, null=True, verbose_name=b'Verwendete W\xc3\xa4hrung bei Finanzangaben'),
        ),
        migrations.AddField(
            model_name='historicalreport',
            name='currency_rate',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=4, verbose_name=b'W\xc3\xa4hrungskurs zu USD'),
        ),
        migrations.AddField(
            model_name='report',
            name='currency',
            field=models.CharField(default=b'', max_length=10, null=True, verbose_name=b'Verwendete W\xc3\xa4hrung bei Finanzangaben'),
        ),
        migrations.AddField(
            model_name='report',
            name='currency_rate',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=4, verbose_name=b'W\xc3\xa4hrungskurs zu USD'),
        ),
        migrations.AlterField(
            model_name='historicalreport',
            name='economic_payment_types',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(b'cash', b'Cash Payment'), (b'installment', b'Installment'), (b'card', b'Payment with Credit/Debit Card'), (b'phone', b'Payment with Mobile Phone'), (b'microloan', b'Micro Loan (e.g. in cooperation with Micro Finance Institution)'), (b'other', b'Other')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='economic_payment_types',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(b'cash', b'Cash Payment'), (b'installment', b'Installment'), (b'card', b'Payment with Credit/Debit Card'), (b'phone', b'Payment with Mobile Phone'), (b'microloan', b'Micro Loan (e.g. in cooperation with Micro Finance Institution)'), (b'other', b'Other')], max_length=20, null=True),
        ),
    ]