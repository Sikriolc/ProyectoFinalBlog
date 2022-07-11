import datetime
from django.db import models
from AppInterface.models import *
from multiselectfield import MultiSelectField


# Create your models here.

class Noticia(models.Model):
  titulo=models.CharField(max_length=100)
  subtitulo=models.CharField(max_length=100)
  fecha=datetime.datetime.now()  
  categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
  imagen=models.ImageField(upload_to="imagenes/",verbose_name="imagen",null=True)
  cuerpo=models.TextField(null=True)

