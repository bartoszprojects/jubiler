# Generated by Django 2.0.3 on 2018-04-10 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20180410_1920'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mainproducts',
            options={'verbose_name': 'Produkty', 'verbose_name_plural': 'Produkty'},
        ),
        migrations.AlterModelOptions(
            name='productscategory',
            options={'verbose_name': 'Kategorie produktów', 'verbose_name_plural': 'Kategorie produktów'},
        ),
    ]