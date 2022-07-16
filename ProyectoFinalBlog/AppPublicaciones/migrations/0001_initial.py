# Generated by Django 4.0.5 on 2022-07-16 00:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('subtitulo', models.CharField(max_length=100)),
                ('fecha', models.DateField(default=django.utils.timezone.now)),
                ('hora', models.TimeField(default=django.utils.timezone.now)),
                ('imagen', models.ImageField(upload_to='imagenes/publicaciones', verbose_name='imagenpublicacion')),
                ('cuerpo', models.TextField()),
                ('autor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
