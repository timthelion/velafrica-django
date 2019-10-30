# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-09-02 11:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
import velafrica.bikes.models
import velafrica.core.storage


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('velafrica_sud', '0002_auto_20190326_2313'),
        ('stock', '0002_auto_20190326_2309'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.CharField(default=velafrica.bikes.models.bike_id, max_length=255, primary_key=True, serialize=False, unique=True)),
                ('number', models.IntegerField(default=velafrica.bikes.models.next_a_plus_number, unique=True, verbose_name='Nr.')),
                ('type', models.CharField(choices=[('', '-'), ('MTB', 'MTB'), ('TW', 'Touring Woman'), ('TM', 'Touring Man'), ('K', 'Kids'), ('C', 'Classic'), ('R', 'Racing')], max_length=255, null=True, verbose_name='Kategorie')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Datum')),
                ('visum', models.CharField(blank=True, max_length=255, verbose_name='Visum')),
                ('a_plus', models.BooleanField(default=False, verbose_name='A+')),
                ('brand', models.CharField(blank=True, default='', max_length=255, verbose_name='Marke')),
                ('gearing', models.CharField(blank=True, default='', max_length=255, verbose_name='Schaltung')),
                ('drivetrain', models.CharField(blank=True, default='', max_length=255, verbose_name='Gänge')),
                ('type_of_brake', models.CharField(blank=True, choices=[('', '-'), ('hd', 'hydraulic disc'), ('rb', 'rim brake'), ('hrb', 'rim brake')], default='', max_length=255, verbose_name='Bremsentyp')),
                ('brake', models.CharField(blank=True, default='', max_length=255, verbose_name='Marke der Bremsen')),
                ('colour', models.CharField(blank=True, default='', max_length=255, verbose_name='Farbe')),
                ('size', models.CharField(blank=True, choices=[('', '-'), ('S', 'S'), ('M', 'M'), ('L', 'L')], default='', max_length=255, verbose_name='Grösse')),
                ('suspension', models.CharField(blank=True, max_length=255, null=True, verbose_name='Federung')),
                ('extraordinary', models.CharField(blank=True, max_length=255, null=True, verbose_name='Spezielles')),
                ('image', models.ImageField(blank=True, null=True, storage=velafrica.core.storage.MyStorage(), upload_to=velafrica.bikes.models.bike_images, verbose_name='Bild')),
                ('date_created', models.DateField(auto_now_add=True, null=True)),
                ('date_modified', models.DateField(auto_now=True, null=True)),
                ('container', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='velafrica_sud.Container', verbose_name='Container')),
                ('warehouse', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock.Warehouse', verbose_name='Lager')),
            ],
        ),
    ]