# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-09 15:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import velafrica.collection.models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectioneventtaskprogress',
            name='status',
            field=models.ForeignKey(blank=True, default=velafrica.collection.models.get_default_task_status, null=True, on_delete=django.db.models.deletion.CASCADE, to='collection.CollectionEventTaskStatus'),
        ),
    ]
