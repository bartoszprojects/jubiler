# Generated by Django 2.0.3 on 2018-03-18 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20180318_2353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productscategory',
            name='category',
        ),
        migrations.AddField(
            model_name='productscategory',
            name='category',
            field=models.ManyToManyField(default='', null=True, related_name='category', to='products.MainProducts'),
        ),
    ]