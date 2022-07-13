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

class PlusUser(models.Model):
  
  usuario=models.OneToOneField(User, on_delete=models.CASCADE)
  nick_name=models.CharField(max_length=20,null=True)
  fecha_nacimiento=models.DateField(null=True)
  foto_perfil=models.ImageField(upload_to="imagenes/fotosperfil",verbose_name="foto_perfil",null=True, default='imagenes/fotosperfil/foto perfil default.jpg')
  biografia=models.TextField(null=True)

  def __str__(self):
    fecha = str(self.fecha_nacimiento)
    fila = "Apodo: " + self.nick_name + "Biografia" + self.biografia + fecha
    return fila
  
  def delete(self, using=None, keep_parents=False):
    self.foto_perfil.storage.delete(self.foto_perfil.name)
    super().delete()



  