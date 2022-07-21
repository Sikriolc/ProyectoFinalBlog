from email.policy import default
from urllib import request
from django.test import TestCase
from .models import Publicacion
import datetime as datetime_orig


# Create your tests here.

class NoticiasTest(TestCase):

    def Setup(self):
        Publicacion.objects.create(titulo='Publicacion Test',
        autor='admin',
        subtitulo='Esta publicacion es de test',
        fecha=21/7/2022,
        hora=datetime_orig.datetime.now(),
        imagen="",
        cuerpo='Testeando modelo Publicaciones',)

    def test_publicacion_titulo(self):
        publicacion = Publicacion.objects.get(titulo='Publicacion Test')
        self.assertEqual(publicacion.cuerpo, 'Testeando modelo Publicaciones')
    
    def test_publicacion_creada(self):
        publicacion = Publicacion.objects.get(titulo='Publicacion Test')
        self.assertNotEquals(publicacion, None)