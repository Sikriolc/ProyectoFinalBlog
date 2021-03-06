from django.contrib import admin
from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('inicio', views.inicio, name="inicio"),
    path('accounts/login/', views.login_request, name="login"),
    path('logout', views.logout_request, name="logout"),
    path('accounts/signup', views.register_request, name="register"),
    path('editarperfil', views.editar_PlusUser, name="editarperfil"),
    path('accounts/profile', views.perfil, name="perfil"),


    path('categorias', views.categorias, name="categorias"),
    path('crearcategoria', views.categorias_crear, name="crearcategoria"),
    path('buscarcategoria', views.categoria_buscar, name="buscarcategoria"),
    path('editarcategoria/<int:id>', views.categorias_editar, name="editarcategoria"),
    path('eliminar/<int:id>', views.categorias_eliminar, name="eliminarcategoria"),

    path('about', views.nosotros, name="about"),
    path('contacto', views.contacto, name="contacto"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
