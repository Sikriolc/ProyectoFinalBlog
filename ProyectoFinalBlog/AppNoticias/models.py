import datetime
from xmlrpc.client import DateTime
from django.utils import timezone
from django.db import models
from ckeditor.fields import RichTextField
from AppInterface.models import *


# Create your models here.

class Noticia(models.Model):
  autor=models.ForeignKey(User,blank=True,null=True, on_delete=models.SET_NULL)#para enlazar con usuario logeado tirar ForeignKey, y pasarle captura del error a Lucas
  titulo=models.CharField(max_length=100)
  subtitulo=models.CharField(max_length=100)
  fecha=models.DateField(default=timezone.now)
  hora=models.TimeField(default=timezone.now)
  categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
  imagen=models.ImageField(upload_to="imagenes/",verbose_name="imagen")
  cuerpo=RichTextField(blank=True, null=True)
  
  def __str__(self):
    fila = "Titulo: " + self.titulo + "-" + "Subtitulo: "+self.subtitulo + " - "
    return fila
