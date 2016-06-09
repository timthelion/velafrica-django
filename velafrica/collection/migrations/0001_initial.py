# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-09 14:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organisation', '0006_auto_20160609_1626'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollectionEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('time', models.CharField(max_length=255)),
                ('host', models.CharField(max_length=255)),
                ('notes', models.TextField()),
                ('presence_velafrica', models.CharField(max_length=255)),
                ('pickup', models.CharField(max_length=255)),
                ('processing', models.CharField(max_length=255)),
                ('organisation_done', models.BooleanField(default=False)),
                ('website', models.URLField()),
                ('velo_amount', models.IntegerField()),
                ('people_amount', models.IntegerField()),
                ('hours_amount', models.IntegerField()),
                ('additional_results', models.TextField()),
                ('ort', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organisation.Municipality')),
            ],
        ),
        migrations.CreateModel(
            name='CollectionEventTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CollectionEventTaskProgress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CollectionEventTaskStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('is_default', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CollectionEventType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CollectionPartner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='collectioneventtaskprogress',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='collection.CollectionEventTaskStatus'),
        ),
        migrations.AddField(
            model_name='collectioneventtaskprogress',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collection.CollectionEventTask'),
        ),
    ]
