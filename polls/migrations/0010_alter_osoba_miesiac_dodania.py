# Generated by Django 4.2.7 on 2023-11-07 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_team_person_month_added_alter_person_shirt_size_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='osoba',
            name='miesiac_dodania',
            field=models.DateField(default=11),
        ),
    ]
