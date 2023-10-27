# Generated by Django 4.2.6 on 2023-10-27 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stanowisko',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=100)),
                ('stanowisko', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Osoba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=60)),
                ('nazwisko', models.CharField(max_length=60)),
                ('plec', models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('H', 'HelikopterSzturmowy')], max_length=1)),
                ('stanowisko', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.stanowisko')),
            ],
        ),
    ]
