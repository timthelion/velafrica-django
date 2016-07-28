# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-25 07:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0019_auto_20160722_1712'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalpurchaseorder',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='historicalpurchaseorder',
            name='product',
        ),
        migrations.RemoveField(
            model_name='purchaseorder',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='purchaseorder',
            name='product',
        ),
        migrations.AlterField(
            model_name='invoicelistpos',
            name='amount',
            field=models.IntegerField(default=0, verbose_name=b'St\xc3\xbcckzahl'),
        ),
        migrations.AlterField(
            model_name='purchaseorderlistpos',
            name='amount',
            field=models.IntegerField(default=0, verbose_name=b'St\xc3\xbcckzahl'),
        ),
        migrations.AlterField(
            model_name='salesorderlistpos',
            name='amount',
            field=models.IntegerField(default=0, verbose_name=b'St\xc3\xbcckzahl'),
        ),
        migrations.AlterField(
            model_name='stockchangelistpos',
            name='amount',
            field=models.IntegerField(default=0, verbose_name=b'St\xc3\xbcckzahl'),
        ),
        migrations.AlterField(
            model_name='stocktransferlistpos',
            name='amount',
            field=models.IntegerField(default=0, verbose_name=b'St\xc3\xbcckzahl'),
        ),
        migrations.AlterUniqueTogether(
            name='invoicelistpos',
            unique_together=set([('invoice', 'product')]),
        ),
        migrations.AlterUniqueTogether(
            name='stocktransferlistpos',
            unique_together=set([('stocktransfer', 'product')]),
        ),
    ]
