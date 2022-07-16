from django.contrib import admin
from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('noticias', views.noticias, name="noticias"),
    path('crearnoticia', views.noticia_crear, name="crearnoticia"),
    path('editarnoticia', views.noticia_editar, name="crearnoticia"),
    path('buscarnoticia', views.noticia_buscar, name="buscarnoticia"),


]
