import datetime
from xmlrpc.client import DateTime
from django.utils import timezone
from django.db import models
from AppInterface.models import *


# Create your models here.

class Noticia(models.Model):
  autor=models.CharField(max_length=100)#para enlazar con usuario logeado tirar ForeignKey, y pasarle captura del error a Lucas
  titulo=models.CharField(max_length=100)
  subtitulo=models.CharField(max_length=100)
  fecha=models.DateField(default=timezone.now)
  hora=models.TimeField(default=timezone.now)
  categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
  imagen=models.ImageField(upload_to="imagenes/",verbose_name="imagen")
  cuerpo=models.TextField()
  
  def __str__(self):
    fila = "Titulo: " + self.titulo + "-" + "Subtitulo: "+self.subtitulo + " - " + "Autor: " + self.autor
    return fila
