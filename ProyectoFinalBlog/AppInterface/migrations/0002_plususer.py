# Generated by Django 4.0.5 on 2022-07-11 21:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppInterface', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlusUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick_name', models.CharField(blank=True, max_length=20, null=True)),
                ('fecha_nacimiento', models.DateTimeField(blank=True, null=True)),
                ('foto_perfil', models.ImageField(null=True, upload_to='imagenes/fotosperfil', verbose_name='icono')),
                ('biografia', models.TextField(null=True)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]