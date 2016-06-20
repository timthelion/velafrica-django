# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-13 12:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0014_collectionevent_collection_partner_confirmed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collectionevent',
            old_name='presence_velafrica',
            new_name='presence_velafrica_info',
        ),
        migrations.AlterField(
            model_name='collectionevent',
            name='collection_partner_vrn',
            field=models.ForeignKey(blank=True, help_text=b'Velafrica Partner der die Velos abholt', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='collection_organisation', to='organisation.Organisation', verbose_name=b'Abtransport durch VRN Partner'),
        ),
        migrations.AlterField(
            model_name='collectionevent',
            name='processing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='processing_organisation', to='organisation.Organisation', verbose_name=b'Velo Verarbeitung'),
        ),
    ]