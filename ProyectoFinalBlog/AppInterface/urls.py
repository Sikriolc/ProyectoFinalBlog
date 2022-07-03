from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('inicio', views.inicio, name="inicio"),
    path('categorias', views.categorias, name="categorias"),
    path('nosotros', views.nosotros, name="nosotros"),
    path('contacto', views.contacto, name="contacto"),
]
