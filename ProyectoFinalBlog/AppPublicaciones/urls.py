from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('publicaciones', views.publicaciones, name="publicaciones"),
    path('crearpublicacion', views.publicacion_crear, name="crearpublicacion"),
    path('editarpublicacion/<int:id>', views.publicacion_editar, name="editarpublicacion"),
    path('eliminarpublicacion/<int:id>', views.publicacion_eliminar, name="eliminarpublicacion"),
    path('buscarpublicacion', views.publicacion_buscar, name="buscarpublicacion"),


]
