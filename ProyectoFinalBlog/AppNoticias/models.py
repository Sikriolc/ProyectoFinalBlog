from datetime import datetime
from django.db import models
from AppInterface.models import *
from multiselectfield import MultiSelectField


# Create your models here.

class Noticia(models.Model):
  titulo=models.CharField(max_length=100)
  subtitulo=models.CharField(max_length=100)
  fecha=datetime.now()

  MY_CHOICES2 = (
                (1, 'Item title 2.1'),
                (2, 'Item title 2.2'),
                (3, 'Item title 2.3'),
                (4, 'Item title 2.4'),
                (5, 'Item title 2.5')
                )

  categoria=MultiSelectField(choices = MY_CHOICES2)

  imagen=models.ImageField(upload_to="imagenes/",verbose_name="imagen",null=True)
  cuerpo=models.TextField(null=True)

