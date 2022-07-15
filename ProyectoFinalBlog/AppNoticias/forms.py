from django import forms
from .models import *
from wsgiref.handlers import format_date_time


class NoticiaForm(forms.ModelForm):
  autor=forms.CharField(max_length=100)
  titulo=forms.CharField(max_length=100)
  subtitulo=forms.CharField(max_length=100)
  fecha=forms.DateField()
  hora=forms.TimeField()
  categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
  imagen=forms.ImageField(label="Imagen Noticia", required=False)
  cuerpo=forms.CharField(max_length=1500)

  class Meta:
        model = Noticia
        fields = ['autor','titulo','subtitulo','fecha','hora','categoria','imagen','cuerpo']

    



