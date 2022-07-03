from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('inicio', views.inicio, name="inicio"),

    path('categorias', views.categorias, name="categorias"),
    path('crearcategoria', views.categorias_crear, name="categorias_crear"),
    path('editarcategoria', views.categorias_editar, name="categorias_editar"),

    path('nosotros', views.nosotros, name="nosotros"),
    path('contacto', views.contacto, name="contacto"),
]
