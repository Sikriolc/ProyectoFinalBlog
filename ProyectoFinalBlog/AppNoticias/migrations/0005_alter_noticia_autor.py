# Generated by Django 4.0.5 on 2022-07-12 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppNoticias', '0004_noticia_autor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='autor',
            field=models.CharField(max_length=100),
        ),
    ]