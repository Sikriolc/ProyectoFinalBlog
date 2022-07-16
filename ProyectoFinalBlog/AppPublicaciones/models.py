from django.db import models
import datetime
from xmlrpc.client import DateTime
from django.utils import timezone
from AppInterface.models import *

class Publicacion(models.Model):
  autor=models.ForeignKey(User,blank=True,null=True, on_delete=models.SET_NULL)
  titulo=models.CharField(max_length=100)
  subtitulo=models.CharField(max_length=100)
  fecha=models.DateField(default=timezone.now)
  hora=models.TimeField(default=timezone.now)
  imagen=models.ImageField(upload_to="imagenes/publicaciones",verbose_name="imagenpublicacion")
  cuerpo=models.TextField()
  
  def __str__(self):
    fila = "Titulo: " + self.titulo + " - " + "Autor: " 
    return fila
