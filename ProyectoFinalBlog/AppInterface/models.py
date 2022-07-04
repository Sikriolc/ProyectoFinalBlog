from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
  titulo = models.CharField(max_length=50, verbose_name="titulo")
  detalle = models.CharField(max_length=100,verbose_name="detalle")
  icono = models.ImageField(upload_to="imagenes/",verbose_name="icono",null=True)

  def __str__(self):
    fila = "Titulo: " + self.titulo + "-" + self.detalle
    return fila

  def delete(self, using=None, keep_parents=False):
    self.icono.storage.delete(self.icono.name)
    super().delete()

  