# Generated by Django 2.0.3 on 2018-05-19 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slider', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutinformations',
            options={'verbose_name': 'Podstrona O firmie', 'verbose_name_plural': 'Podstrona O firmie'},
        ),
        migrations.AlterModelOptions(
            name='minisliderofferengraving',
            options={'verbose_name': 'Strona Główna - Slajder: Grawerowanie', 'verbose_name_plural': 'Strona Główna - Slajder: Grawerowanie'},
        ),
        migrations.AlterModelOptions(
            name='minisliderofferindividual',
            options={'verbose_name': 'Strona Główna - Slajder: Na zamówienie', 'verbose_name_plural': 'Strona Główna - Slajder: Na zamówienie'},
        ),
        migrations.AlterModelOptions(
            name='minisliderofferrepair',
            options={'verbose_name': 'Strona Główna - Slajder: Naprawa', 'verbose_name_plural': 'Strona Główna - Slajder: Naprawa'},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={},
        ),
        migrations.AlterModelOptions(
            name='serviceimages',
            options={},
        ),
    ]
