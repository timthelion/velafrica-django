# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-27 11:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0023_auto_20160727_0955'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('received_on', models.DateField(default=django.utils.timezone.now, verbose_name=b'Eingangsdatum')),
                ('amount', models.IntegerField()),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Invoice')),
            ],
        ),
        migrations.AlterField(
            model_name='historicalpurchaseorder',
            name='state',
            field=models.CharField(choices=[(b'3', b'invoiced'), (b'2', b'shipped'), (b'4', b'complete'), (b'0', b'draft'), (b'1', b'confirmed')], default=b'0', max_length=2, verbose_name=b'Status'),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='state',
            field=models.CharField(choices=[(b'3', b'invoiced'), (b'2', b'shipped'), (b'4', b'complete'), (b'0', b'draft'), (b'1', b'confirmed')], default=b'0', max_length=2, verbose_name=b'Status'),
        ),
    ]
