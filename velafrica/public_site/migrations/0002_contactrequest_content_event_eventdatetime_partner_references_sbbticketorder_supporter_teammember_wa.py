# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-10-19 12:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0001_initial'),
        ('collection', '0001_initial'),
        ('public_site', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name=b'Vorname')),
                ('last_name', models.CharField(max_length=255, verbose_name=b'Nachname')),
                ('email', models.CharField(max_length=255, verbose_name=b'E-Mail')),
                ('phone', models.CharField(blank=True, max_length=255, verbose_name=b'Telefonnummer')),
                ('note', models.TextField(verbose_name=b'Nachricht')),
            ],
            options={
                'verbose_name': 'Kontaktanfrage',
                'verbose_name_plural': 'Kontaktanfragen',
            },
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=2, verbose_name=b'Sprache')),
                ('path', models.CharField(max_length=255, verbose_name=b'Pfad')),
                ('key', models.CharField(max_length=255, verbose_name=b'Key')),
                ('value', models.TextField(blank=True, verbose_name=b'Value')),
                ('description', models.TextField(blank=True, verbose_name=b'Beschreibung')),
            ],
            options={
                'verbose_name': 'Inhalt',
                'verbose_name_plural': 'Inhalte',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name=b'Name')),
                ('description', models.TextField(blank=True, verbose_name=b'Beschreibung')),
                ('organizer', models.CharField(blank=True, max_length=255, verbose_name=b'Veranstalter')),
                ('active', models.BooleanField(default=True, verbose_name=b'Aktiv')),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pub_event_address', to='organisation.Address', verbose_name=b'Adresse')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pub_event_category', to='collection.EventCategory', verbose_name=b'Kategorie')),
            ],
            options={
                'verbose_name': 'Veranstaltung',
                'verbose_name_plural': 'Veranstaltungen',
            },
        ),
        migrations.CreateModel(
            name='EventDateTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name=b'Datum')),
                ('time_start', models.CharField(blank=True, max_length=255, verbose_name=b'Von')),
                ('time_end', models.CharField(blank=True, max_length=255, verbose_name=b'Bis')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='datetimes', to='public_site.Event')),
            ],
            options={
                'ordering': ['date'],
                'verbose_name': 'Datum/Uhrzeit',
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name=b'Name')),
                ('category', models.CharField(blank=True, max_length=255, verbose_name=b'Kategorie/Bereich')),
                ('description', models.TextField(blank=True, verbose_name=b'Beschreibung')),
                ('link', models.CharField(blank=True, max_length=255, verbose_name=b'URL')),
                ('image', models.URLField(verbose_name=b'Bild URL')),
                ('teaserd', models.BooleanField(default=False, verbose_name=b'Teaser')),
                ('country', models.IntegerField(choices=[(1, b'Afrika'), (2, b'Schweiz')], verbose_name=b'Land')),
                ('location', models.CharField(max_length=255, verbose_name=b'Kanton/Staat')),
                ('city', models.CharField(max_length=255, verbose_name=b'Stadt')),
            ],
            options={
                'verbose_name': 'Partner',
                'verbose_name_plural': 'Partner',
            },
        ),
        migrations.CreateModel(
            name='References',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Name')),
                ('image', models.CharField(max_length=255, verbose_name=b'Bild-URL')),
                ('text', models.TextField(verbose_name=b'Text')),
                ('sorting', models.IntegerField(default=0, verbose_name=b'Sortierung')),
            ],
            options={
                'verbose_name': 'Botschafter',
                'verbose_name_plural': 'Botschafter',
            },
        ),
        migrations.CreateModel(
            name='SbbTicketOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name=b'Vorname')),
                ('last_name', models.CharField(max_length=255, verbose_name=b'Nachname')),
                ('address', models.CharField(max_length=255, verbose_name=b'Strasse und Hausnummer')),
                ('zip', models.CharField(max_length=255, verbose_name=b'PLZ und Ort')),
                ('email', models.CharField(max_length=255, verbose_name=b'E-Mail')),
                ('phone', models.CharField(blank=True, max_length=255, verbose_name=b'Telefonnummer')),
                ('note', models.TextField(blank=True, verbose_name=b'Bemerkung')),
                ('amount', models.IntegerField(default=1, verbose_name=b'Anzahl')),
                ('dropoff', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='collection.Dropoff')),
            ],
            options={
                'verbose_name': 'SBB Ticketbestellung',
                'verbose_name_plural': 'SBB Ticketbestellungen',
            },
        ),
        migrations.CreateModel(
            name='Supporter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name=b'Name')),
                ('description', models.CharField(blank=True, help_text=b'Max. 140 Zeichen', max_length=140, verbose_name=b'Kurzbeschreibung')),
                ('link', models.URLField(verbose_name=b'URL')),
                ('image', models.CharField(blank=True, max_length=255, verbose_name=b'Bild/Logo URL')),
                ('sorting', models.IntegerField(default=0, verbose_name=b'Sortierung')),
                ('active', models.BooleanField(default=True, verbose_name=b'Aktiv')),
            ],
            options={
                'verbose_name': 'Unterst\xfctzer',
                'verbose_name_plural': 'Unterst\xfctzer',
            },
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Name')),
                ('position', models.CharField(blank=True, max_length=255, verbose_name=b'Position')),
                ('email', models.CharField(blank=True, max_length=255, verbose_name=b'E-Mail')),
                ('phone', models.CharField(blank=True, max_length=255, verbose_name=b'Telefonnummer')),
                ('image', models.CharField(blank=True, max_length=255, verbose_name=b'Bild-URL')),
                ('sorting', models.IntegerField(default=0, verbose_name=b'Sortierung')),
            ],
            options={
                'verbose_name': 'Teammitglied',
                'verbose_name_plural': 'Teammitglieder',
            },
        ),
        migrations.CreateModel(
            name='WalkthroughRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name=b'Vorname')),
                ('last_name', models.CharField(max_length=255, verbose_name=b'Nachname')),
                ('phone', models.CharField(max_length=255, verbose_name=b'Telefonnummer')),
                ('email', models.CharField(max_length=255, verbose_name=b'E-Mail')),
                ('organizer_type', models.IntegerField(choices=[(1, b'Verein'), (2, b'Firma'), (3, b'Gemeinde'), (4, b'Kirchgemeinde'), (5, b'Schule'), (6, b'Liegenschaftsverwaltung'), (7, b'Privatperson'), (8, b'Andere')], default=1, verbose_name=b'Veranstalter')),
                ('collected_before', models.BooleanField(default=False, verbose_name=b'Bereits f\xc3\xbcr Velafrica gesammelt')),
                ('collected_before_note', models.TextField(blank=True, verbose_name=b'Wann und wo')),
                ('date_fixed', models.BooleanField(default=False, verbose_name=b'Datum fixiert')),
                ('date', models.DateField(blank=True, null=True, verbose_name=b'Datum')),
                ('pickup_time_start', models.CharField(blank=True, max_length=255, verbose_name=b'Annahmezeit von')),
                ('pickup_time_end', models.CharField(blank=True, max_length=255, verbose_name=b'Annahmezeit bis')),
                ('address', models.CharField(blank=True, max_length=255, verbose_name=b'Adresse')),
                ('zip', models.CharField(blank=True, max_length=255, verbose_name=b'Postleitzahl')),
                ('address_note', models.TextField(blank=True, verbose_name=b'Standortbeschreibung')),
                ('expected_velos', models.IntegerField(choices=[(1, b'1 - 20'), (2, b'21 - 50'), (3, b'51 - 100'), (4, b'101 - 1000'), (5, b'> 1000')], default=1, verbose_name=b'Erwartete Menge gesammelter Velos')),
                ('can_store', models.BooleanField(default=False, verbose_name=b'Kann Velos vor Ort zwischenlagern')),
                ('can_deliver', models.BooleanField(default=False, verbose_name=b'Kann Abtransport zu Partner \xc3\xbcbernehmen')),
                ('velafrica_pickup', models.BooleanField(default=False, verbose_name=b'Abtransport durch Velafrica')),
                ('responsible_first_name', models.CharField(blank=True, max_length=255, verbose_name=b'Vorname')),
                ('responsible_last_name', models.CharField(blank=True, max_length=255, verbose_name=b'Nachname')),
                ('responsible_phone', models.CharField(blank=True, max_length=255, verbose_name=b'Telefonnummer')),
                ('responsible_email', models.CharField(blank=True, max_length=255, verbose_name=b'E-Mail')),
                ('supporter_count', models.IntegerField(choices=[(1, b'1 - 10'), (2, b'11 - 20'), (3, b'21 - 30'), (4, b'31 - 40'), (4, b'41 - 50')], default=1, verbose_name=b'Anzahl Helfer')),
                ('supporter_note', models.TextField(blank=True, verbose_name=b'Bemerkung')),
            ],
            options={
                'verbose_name': 'Sammelanlassanfrage',
                'verbose_name_plural': 'Sammelanlassanfragen',
            },
        ),
    ]