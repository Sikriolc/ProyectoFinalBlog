from django.contrib import admin
from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('inicio', views.inicio, name="inicio"),
    path('login', views.login_request, name="login"),
    path('logout', views.logout_request, name="logout"),
    path('register', views.register_request, name="register"),

    path('categorias', views.categorias, name="categorias"),
    path('crearcategoria', views.categorias_crear, name="crearcategoria"),
    path('editarcategoria', views.categorias_editar, name="editarcategoria"),

    path('nosotros', views.nosotros, name="nosotros"),
    path('contacto', views.contacto, name="contacto"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
