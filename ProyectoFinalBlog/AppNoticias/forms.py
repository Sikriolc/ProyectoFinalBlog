from django import forms
from .models import *
from wsgiref.handlers import format_date_time
from django.forms.widgets import NumberInput


class NoticiaForm(forms.ModelForm):
  autor=forms.CharField(max_length=100)
  titulo=forms.CharField(max_length=100)
  subtitulo=forms.CharField(max_length=100)
  fecha=forms.DateField(widget=NumberInput(attrs={'type': 'date'}))#https://simpleisbetterthancomplex.com/tutorial/2019/01/03/how-to-use-date-picker-with-django.html
  hora=forms.TimeField(widget=NumberInput(attrs={'type': 'time'}))
  #categoria=forms.ForeignKey(Categoria, on_delete=models.CASCADE)
  imagen=forms.ImageField(label="Imagen Noticia", required=False)
  cuerpo=forms.CharField(max_length=1500, widget=forms.Textarea())

  class Meta:
        model = Noticia
        fields = ['autor','titulo','subtitulo','fecha','hora','categoria','imagen','cuerpo']

    



