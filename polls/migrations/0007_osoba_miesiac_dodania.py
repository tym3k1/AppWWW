# Generated by Django 4.2.6 on 2023-11-06 12:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_rename_stanowisko_stanowisko_opis'),
    ]

    operations = [
        migrations.AddField(
            model_name='osoba',
            name='miesiac_dodania',
            field=models.DateTimeField(default=datetime.date(2023, 11, 1)),
        ),
    ]
