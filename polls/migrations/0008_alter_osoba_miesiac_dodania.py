# Generated by Django 4.2.6 on 2023-11-06 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_osoba_miesiac_dodania'),
    ]

    operations = [
        migrations.AlterField(
            model_name='osoba',
            name='miesiac_dodania',
            field=models.IntegerField(default=11),
        ),
    ]
