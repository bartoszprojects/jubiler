# Generated by Django 2.0.3 on 2018-04-10 23:14

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slider', '0005_auto_20180411_0106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutinformations',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
