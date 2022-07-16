from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('publicaciones', views.publicaciones, name="publicaciones"),
    path('crearpublicacion', views.publicacion_crear, name="crearpublicacion"),

]
