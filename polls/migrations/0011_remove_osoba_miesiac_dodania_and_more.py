# Generated by Django 4.2.7 on 2023-11-08 12:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_alter_osoba_miesiac_dodania'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='osoba',
            name='miesiac_dodania',
        ),
        migrations.AlterField(
            model_name='osoba',
            name='data_dodania',
            field=models.DateTimeField(default=1),
        ),
    ]
