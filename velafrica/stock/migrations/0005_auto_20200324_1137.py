# Generated by Django 2.1.15 on 2020-03-24 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0004_auto_20190925_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockchange',
            name='stock_change_type',
            field=models.CharField(choices=[('out', 'out'), ('in', 'in')], max_length=255),
        ),
    ]
