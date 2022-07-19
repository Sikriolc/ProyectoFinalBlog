from django.contrib import admin
from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
  
    path('noticias', views.noticias, name="noticias"),
    path('noticiasdetalle/<int:id>', views.noticiasdetalle, name="noticiasdetalle"),
    path('crearnoticia', views.noticia_crear, name="crearnoticia"),
    path('editarnoticia/<int:id>', views.noticia_editar, name="editarnoticia"),
    path('buscarnoticia', views.noticia_buscar, name="buscarnoticia"),
    path('eliminarnoticia/<int:id>', views.noticia_eliminar, name="eliminarnoticia"),
    


]
