# Generated by Django 4.0.5 on 2022-07-20 01:55

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppPublicaciones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='cuerpo',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
