# Generated by Django 2.1.12 on 2019-12-31 13:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    replaces = [('transport', '0004_auto_20191219_1147'), ('transport', '0005_auto_20191226_1114'), ('transport', '0006_auto_20191226_1701'), ('transport', '0007_auto_20191226_1705'), ('transport', '0008_auto_20191226_2229'), ('transport', '0009_auto_20191226_2230'), ('transport', '0010_auto_20191231_1357')]

    dependencies = [
        ('transport', '0003_auto_20190925_1956'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(blank=True, default='', max_length=255, verbose_name='Name')),
            ],
            options={
                'verbose_name_plural': 'request categories',
            },
        ),
        migrations.AlterModelOptions(
            name='driver',
            options={'ordering': ['-active', 'name']},
        ),
        migrations.AddField(
            model_name='historicalride',
            name='charged',
            field=models.BooleanField(default=False, verbose_name='Kostenpflichtig'),
        ),
        migrations.AddField(
            model_name='historicalride',
            name='completed',
            field=models.BooleanField(default=False, verbose_name='Auftrag ausgeführt'),
        ),
        migrations.AddField(
            model_name='historicalride',
            name='created_by',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Auftrag erstellt von'),
        ),
        migrations.AddField(
            model_name='historicalride',
            name='customer_city',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Ort'),
        ),
        migrations.AddField(
            model_name='historicalride',
            name='customer_email',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='historicalride',
            name='customer_firstname',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Vorname'),
        ),
        migrations.AddField(
            model_name='historicalride',
            name='customer_lastname',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Nachname'),
        ),
        migrations.AddField(
            model_name='historicalride',
            name='customer_phone',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Telefon'),
        ),
        migrations.AddField(
            model_name='historicalride',
            name='customer_zip_code',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='PLZ'),
        ),
        migrations.AddField(
            model_name='historicalride',
            name='customer_salutation',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Anrede'),
        ),
        migrations.AddField(
            model_name='historicalride',
            name='customer_street_nr',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Strasse, Nr.'),
        ),
        migrations.AddField(
            model_name='historicalride',
            name='date_created',
            field=models.DateField(blank=True, editable=False, null=True, verbose_name='Auftrag erstellt am'),
        ),
        migrations.AddField(
            model_name='historicalride',
            name='date_modified',
            field=models.DateField(blank=True, editable=False, null=True, verbose_name='Bearbeitet am'),
        ),
        migrations.AddField(
            model_name='historicalride',
            name='from_city',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Ort'),
        ),
        migrations.AddField(
            model_name='historicalride',
            name='from_comment',
            field=models.CharField(blank=True, default='', help_text='Bemerkung zum Abholort', max_length=255, verbose_name='Bemerkung'),
        ),
        migrations.AddField(
            model_name='historicalride',
            name='from_contact_name',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Kontaktperson'),
        ),
        migrations.AddField(
            model_name='historicalride',
            name='from_contact_phone',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Telefonnummer'),
        ),
        migrations.AddField(
            model_name='historicalride',
            name='from_street_nr',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Strasse, Nr.'),
        ),
        migrations.AddField(
            model_name='historicalride',
            name='from_zip_code',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='PLZ'),
        ),
        migrations.AddField(
            model_name='historicalride',
            name='invoice_city',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Ort'),
        ),
        migrations.AddField(
            model_name='historicalride',
            name='invoice_commissioned',
            field=models.BooleanField(default=False, verbose_name='Rechnung in Auftrag gegeben'),
        ),
        migrations.AddField(
            model_name='historicalride',
            name='invoice_company_addition',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Firmenzusatz'),
        ),
        migrations.AddField(
            model_name='historicalride',
            name='invoice_company_name',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Firmenname'),
        ),
        migrations.AddField(
            model_name='historicalride',
            name='invoice_same_as_customer',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='historicalride',
            name='invoice_street_nr',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Strasse, Nr.'),
        ),
        migrations.AddField(
            model_name='historicalride',
            name='planned_velos',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Anzahl'),
        ),
        migrations.AddField(
            model_name='historicalride',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Preis'),
        ),
        migrations.AddField(
            model_name='historicalride',
            name='request_comment',
            field=models.CharField(blank=True, default='', help_text='Bemerkung zum Auftrag', max_length=255, verbose_name='Bemerkung'),
        ),
        migrations.AddField(
            model_name='historicalride',
            name='to_city',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Ort'),
        ),
        migrations.AddField(
            model_name='historicalride',
            name='to_comment',
            field=models.CharField(blank=True, default='', help_text='Bemerkung zur Lieferadresse', max_length=255, verbose_name='Bemerkung'),
        ),
        migrations.AddField(
            model_name='historicalride',
            name='to_contact_name',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Kontaktperson'),
        ),
        migrations.AddField(
            model_name='historicalride',
            name='to_street_nr',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Strasse, Nr.'),
        ),
        migrations.AddField(
            model_name='historicalride',
            name='to_zip_code',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='PLZ'),
        ),
        migrations.AddField(
            model_name='ride',
            name='charged',
            field=models.BooleanField(default=False, verbose_name='Kostenpflichtig'),
        ),
        migrations.AddField(
            model_name='ride',
            name='completed',
            field=models.BooleanField(default=False, verbose_name='Auftrag ausgeführt'),
        ),
        migrations.AddField(
            model_name='ride',
            name='created_by',
            field=models.CharField(default='', max_length=255, verbose_name='Auftrag erstellt von'),
        ),
        migrations.AddField(
            model_name='ride',
            name='customer_city',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Ort'),
        ),
        migrations.AddField(
            model_name='ride',
            name='customer_email',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='ride',
            name='customer_firstname',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Vorname'),
        ),
        migrations.AddField(
            model_name='ride',
            name='customer_lastname',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Nachname'),
        ),
        migrations.AddField(
            model_name='ride',
            name='customer_phone',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Telefon'),
        ),
        migrations.AddField(
            model_name='ride',
            name='customer_plz',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='PLZ'),
        ),
        migrations.AddField(
            model_name='ride',
            name='customer_salutation',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Anrede'),
        ),
        migrations.AddField(
            model_name='ride',
            name='customer_street_nr',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Strasse, Nr.'),
        ),
        migrations.AddField(
            model_name='ride',
            name='date_created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='ride',
            name='date_modified',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='ride',
            name='from_city',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Ort'),
        ),
        migrations.AddField(
            model_name='ride',
            name='from_comment',
            field=models.CharField(blank=True, default='', help_text='Bemerkung zum Abholort', max_length=255, verbose_name='Bemerkung'),
        ),
        migrations.AddField(
            model_name='ride',
            name='from_contact_name',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Kontaktperson'),
        ),
        migrations.AddField(
            model_name='ride',
            name='from_contact_phone',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Telefonnummer'),
        ),
        migrations.AddField(
            model_name='ride',
            name='from_street_nr',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Strasse, Nr.'),
        ),
        migrations.AddField(
            model_name='ride',
            name='from_zip_code',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='PLZ'),
        ),
        migrations.AddField(
            model_name='ride',
            name='invoice_city',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Ort'),
        ),
        migrations.AddField(
            model_name='ride',
            name='invoice_commissioned',
            field=models.BooleanField(default=False, verbose_name='Rechnung in Auftrag gegeben'),
        ),
        migrations.AddField(
            model_name='ride',
            name='invoice_company_addition',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Firmenzusatz'),
        ),
        migrations.AddField(
            model_name='ride',
            name='invoice_company_name',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Firmenname'),
        ),
        migrations.AddField(
            model_name='ride',
            name='invoice_plz',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='PLZ'),
        ),
        migrations.AddField(
            model_name='ride',
            name='invoice_same_as_customer',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='ride',
            name='invoice_street_nr',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Strasse, Nr.'),
        ),
        migrations.AddField(
            model_name='ride',
            name='planned_velos',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Anzahl'),
        ),
        migrations.AddField(
            model_name='ride',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Preis'),
        ),
        migrations.AddField(
            model_name='ride',
            name='request_comment',
            field=models.CharField(blank=True, default='', help_text='Bemerkung zum Auftrag', max_length=255, verbose_name='Bemerkung'),
        ),
        migrations.AddField(
            model_name='ride',
            name='to_city',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Ort'),
        ),
        migrations.AddField(
            model_name='ride',
            name='to_comment',
            field=models.CharField(blank=True, default='', help_text='Bemerkung zur Lieferadresse', max_length=255, verbose_name='Bemerkung'),
        ),
        migrations.AddField(
            model_name='ride',
            name='to_contact_name',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Kontaktperson'),
        ),
        migrations.AddField(
            model_name='ride',
            name='to_street_nr',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Strasse, Nr.'),
        ),
        migrations.AddField(
            model_name='ride',
            name='to_zip_code',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='PLZ'),
        ),
        migrations.AlterField(
            model_name='historicalride',
            name='date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Ausführdatum'),
        ),
        migrations.AlterField(
            model_name='historicalride',
            name='note',
            field=models.CharField(blank=True, help_text='Bemerkung zum Fahrt', max_length=255, null=True, verbose_name='Bemerkung'),
        ),
        migrations.AlterField(
            model_name='historicalride',
            name='to_warehouse',
            field=models.ForeignKey(blank=True, db_constraint=False, default='', help_text='Ziel der Fahrt', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='stock.Warehouse', verbose_name='Ziel'),
        ),
        migrations.AlterField(
            model_name='historicalride',
            name='velos',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Anzahl Velos'),
        ),
        migrations.AlterField(
            model_name='ride',
            name='car',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='transport.Car', verbose_name='Fahrzeug'),
        ),
        migrations.AlterField(
            model_name='ride',
            name='date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Ausführdatum'),
        ),
        migrations.AlterField(
            model_name='ride',
            name='driver',
            field=models.ForeignKey(blank=True, help_text='Person die den Transport durchgeführt hat.', null=True, on_delete=django.db.models.deletion.CASCADE, to='transport.Driver', verbose_name='Fahrer'),
        ),
        migrations.AlterField(
            model_name='ride',
            name='from_warehouse',
            field=models.ForeignKey(blank=True, help_text='Start der Fahrt', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='from_warehouse', to='stock.Warehouse', verbose_name='Start'),
        ),
        migrations.AlterField(
            model_name='ride',
            name='note',
            field=models.CharField(blank=True, help_text='Bemerkung zum Fahrt', max_length=255, null=True, verbose_name='Bemerkung'),
        ),
        migrations.AlterField(
            model_name='ride',
            name='to_warehouse',
            field=models.ForeignKey(blank=True, default='', help_text='Ziel der Fahrt', on_delete=django.db.models.deletion.CASCADE, related_name='to_warehouse', to='stock.Warehouse', verbose_name='Ziel'),
        ),
        migrations.AlterField(
            model_name='ride',
            name='velo_state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='transport.VeloState', verbose_name='Zustand der Velos'),
        ),
        migrations.AlterField(
            model_name='ride',
            name='velos',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Anzahl Velos'),
        ),
        migrations.AddField(
            model_name='historicalride',
            name='request_category',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='transport.RequestCategory', verbose_name='Auftragsart'),
        ),
        migrations.AddField(
            model_name='ride',
            name='request_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='transport.RequestCategory', verbose_name='Auftragsart'),
        ),
        migrations.AlterField(
            model_name='ride',
            name='to_warehouse',
            field=models.ForeignKey(blank=True, default='', help_text='Ziel der Fahrt', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='to_warehouse', to='stock.Warehouse', verbose_name='Ziel'),
        ),
        migrations.AlterModelOptions(
            name='ride',
            options={'ordering': ['-completed', '-date', 'date_created']},
        ),
        migrations.RenameField(
            model_name='ride',
            old_name='customer_plz',
            new_name='customer_zip_code',
        ),
        migrations.RemoveField(
            model_name='historicalride',
            name='from_warehouse_detail_address',
        ),
        migrations.RemoveField(
            model_name='historicalride',
            name='to_warehouse_detail_address',
        ),
        migrations.RemoveField(
            model_name='ride',
            name='from_warehouse_detail_address',
        ),
        migrations.RemoveField(
            model_name='ride',
            name='invoice_plz',
        ),
        migrations.RemoveField(
            model_name='ride',
            name='to_warehouse_detail_address',
        ),
        migrations.AlterField(
            model_name='driver',
            name='active',
            field=models.BooleanField(default=True, help_text='Ist der Fahrer noch bei Velafrica? Inaktive Fahrer werden als (inaktiv) in der Auswahl bei den Fahrten aufgeführt.'),
        ),
        migrations.AlterField(
            model_name='historicaldriver',
            name='active',
            field=models.BooleanField(default=True, help_text='Ist der Fahrer noch bei Velafrica? Inaktive Fahrer werden als (inaktiv) in der Auswahl bei den Fahrten aufgeführt.'),
        ),
        migrations.AlterField(
            model_name='historicalride',
            name='to_warehouse',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='Ziel der Fahrt', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='stock.Warehouse', verbose_name='Ziel'),
        ),
        migrations.AlterField(
            model_name='ride',
            name='date_created',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Auftrag erstellt am'),
        ),
        migrations.AlterField(
            model_name='ride',
            name='date_modified',
            field=models.DateField(auto_now=True, null=True, verbose_name='Bearbeitet am'),
        ),
        migrations.AlterField(
            model_name='ride',
            name='to_warehouse',
            field=models.ForeignKey(blank=True, help_text='Ziel der Fahrt', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='to_warehouse', to='stock.Warehouse', verbose_name='Ziel'),
        ),
        migrations.AddField(
            model_name='historicalride',
            name='invoice_zip_code',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='PLZ'),
        ),
        migrations.AddField(
            model_name='ride',
            name='invoice_zip_code',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='PLZ'),
        ),
        migrations.AlterModelOptions(
            name='ride',
            options={'ordering': ['completed', 'invoice_commissioned', '-date', '-date_created']},
        ),
        migrations.AddField(
            model_name='historicalride',
            name='customer_company',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Firma'),
        ),
        migrations.AddField(
            model_name='ride',
            name='customer_company',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Firma'),
        ),
        migrations.AlterModelOptions(
            name='ride',
            options={'ordering': ['completed', '-date', '-date_created']},
        ),
        migrations.AlterField(
            model_name='ride',
            name='created_by',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Auftrag erstellt von'),
        ),
    ]
