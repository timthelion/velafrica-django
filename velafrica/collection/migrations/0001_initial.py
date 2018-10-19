# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-10-19 12:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organisation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollectionEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
                ('time', models.CharField(blank=True, help_text=b'Zeit f\xc3\xbcr Veloannahme', max_length=255, verbose_name=b'Veloannahme')),
                ('notes', models.TextField(blank=True, help_text=b'Sachen die noch zu erledigen sind / Weitere Infos / Bemerkungen', verbose_name=b'To do')),
                ('public', models.BooleanField(default=False, help_text=b'Soll der Event auf der Webseite angezeigt werden?', verbose_name=b'\xc3\x96ffentlich')),
                ('presence_velafrica', models.BooleanField(default=False, verbose_name=b'Pr\xc3\xa4senz Velafrica?')),
                ('presence_velafrica_info', models.CharField(blank=True, help_text=b'Infos zur Pr\xc3\xa4senz von Velafrica am Event', max_length=255, verbose_name=b'Pr\xc3\xa4senz Velafrica')),
                ('collection', models.TextField(blank=True, help_text=b'Infos zur Abholung der Velos', verbose_name=b'Notizen Abtransport')),
                ('processing_notes', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Velo Verarbeitung Notizen')),
                ('collection_partner_other', models.CharField(blank=True, help_text=b'Wenn die Velos nicht von einem Velafrica Partner abgeholt werden, bitte hier eintragen von wem', max_length=255, verbose_name=b'Abtransport durch andere Organisation')),
                ('collection_partner_confirmed', models.BooleanField(default=False, verbose_name=b'Transport best\xc3\xa4tigt?')),
                ('intermediate_store', models.BooleanField(default=False, verbose_name=b'Zwischenlagerung m\xc3\xb6glich?')),
                ('website', models.URLField(blank=True, help_text=b'Website des Events')),
                ('feedback', models.BooleanField(default=False, verbose_name=b'Feedback eingeholt?')),
                ('velo_amount', models.IntegerField(default=0, help_text=b'Anzahl gesammelter Velos', verbose_name=b'Anzahl Velos')),
                ('people_amount', models.IntegerField(default=0, verbose_name=b'Anzahl Helfer vor Ort')),
                ('hours_amount', models.IntegerField(default=0, help_text=b'Anzahl geleistete Stunden von allen Helfern zusammen', verbose_name=b'Geleistete Stunden')),
                ('money_amount', models.IntegerField(default=0, help_text=b'Betrag in CHF der am Event gesammelt wurde', verbose_name=b'Gesammeltes Geld')),
                ('additional_results', models.TextField(blank=True, help_text=b'Zus\xc3\xa4tzliche Resultate / Erkenntnisse, m\xc3\xbcndlichesFeedback, etc', verbose_name=b'weitere Resultate')),
                ('material_returned', models.BooleanField(default=False, verbose_name=b'Material retour?')),
                ('material_returned_notes', models.TextField(blank=True, null=True, verbose_name=b'Bemerkungen zu Material Retournierung')),
                ('complete', models.BooleanField(default=False, verbose_name=b'Abgeschlossen')),
                ('address_notes', models.TextField(blank=True)),
                ('address_new', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organisation.Address', verbose_name=b'Adresse')),
                ('collection_partner_vrn', models.ForeignKey(blank=True, help_text=b'Velafrica Partner der die Velos abholt', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='collection_organisation', to='organisation.Organisation', verbose_name=b'Abtransport durch VRN Partner')),
            ],
            options={
                'ordering': ['date_start'],
                'verbose_name': 'Sammelanlass',
                'verbose_name_plural': 'Sammelanl\xe4sse',
            },
        ),
        migrations.CreateModel(
            name='Dropoff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name=b'Name der Sammelstelle')),
                ('active', models.BooleanField(default=True, verbose_name=b'Aktiv')),
                ('sbb', models.BooleanField(default=False, verbose_name=b'SBB')),
                ('contact_person', models.CharField(blank=True, max_length=255, verbose_name=b'Kontaktperson')),
                ('phone_number', models.CharField(blank=True, max_length=255, verbose_name=b'Telefonnummer')),
                ('temp', models.BooleanField(default=False, verbose_name=b'Tempor\xc3\xa4r')),
                ('temp_start', models.DateField(blank=True, null=True, verbose_name=b'Tempor\xc3\xa4r Start')),
                ('temp_end', models.DateField(blank=True, null=True, verbose_name=b'Tempor\xc3\xa4r Ende')),
                ('opening_time', models.TextField(blank=True, verbose_name=b'\xc3\x96ffnungszeiten')),
                ('notes', models.TextField(blank=True, verbose_name=b'Optionale Textinfo')),
                ('custom_lat', models.CharField(blank=True, max_length=255, verbose_name=b'Latitude')),
                ('custom_lon', models.CharField(blank=True, max_length=255, verbose_name=b'Longitude')),
                ('pickup', models.BooleanField(default=False, verbose_name=b'Abholservice')),
                ('pickup_description', models.TextField(blank=True, verbose_name=b'Abholservice Beschreibung')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organisation.Address', verbose_name=b'Adresse')),
            ],
            options={
                'verbose_name': 'Abgabstelle',
                'verbose_name_plural': 'Abgabstellen',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True, verbose_name=b'Beschreibung')),
                ('yearly', models.BooleanField(default=False, verbose_name=b'J\xc3\xa4hrlich wiederkehrend?')),
                ('host', models.CharField(max_length=255, verbose_name=b'Veranstalter')),
                ('contact', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Kontaktperson')),
                ('address_notes', models.TextField(blank=True, verbose_name=b'Genauer Standort')),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organisation.Address', verbose_name=b'Adresse')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Event',
            },
        ),
        migrations.CreateModel(
            name='EventCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text=b'Name der Kategorie', max_length=255, unique=True)),
            ],
            options={
                'ordering': ['-name'],
                'verbose_name': 'Event Kategorie',
                'verbose_name_plural': 'Event Kategorien',
            },
        ),
        migrations.CreateModel(
            name='HostType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text=b'Name der Veranstalter Kategorie', max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'Veranstalter Kategorie',
                'verbose_name_plural': 'Veranstalter Kategorien',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TaskProgress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.TextField(blank=True, verbose_name=b'Notizen')),
                ('status', models.BooleanField(default=False, verbose_name=b'Erledigt?')),
                ('collection_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collection.CollectionEvent')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collection.Task')),
            ],
            options={
                'verbose_name': 'Task Fortschritt',
                'verbose_name_plural': 'Task Fortschritte',
            },
        ),
        migrations.AddField(
            model_name='event',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collection.EventCategory', verbose_name=b'Kategorie'),
        ),
        migrations.AddField(
            model_name='event',
            name='host_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='collection.HostType', verbose_name=b'Veranstalter Typ'),
        ),
        migrations.AddField(
            model_name='event',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='collection.Region', verbose_name=b'Region'),
        ),
        migrations.AddField(
            model_name='collectionevent',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collection.Event'),
        ),
        migrations.AddField(
            model_name='collectionevent',
            name='processing',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='processing_organisation', to='organisation.Organisation', verbose_name=b'Velo Verarbeitung'),
        ),
    ]
