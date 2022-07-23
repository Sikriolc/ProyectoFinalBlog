from django import forms
from .models import *
from wsgiref.handlers import format_date_time
from django.forms.widgets import NumberInput
from ckeditor.widgets import CKEditorWidget

#Formulario de la Noticia

class NoticiaForm(forms.ModelForm):
  titulo=forms.CharField(max_length=100)
  subtitulo=forms.CharField(max_length=100)
  fecha=forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
  hora=forms.TimeField(widget=NumberInput(attrs={'type': 'time'}))
  imagen=forms.ImageField(label="Imagen Noticia", required=False)
  

  class Meta:
        model = Noticia
        fields = ['titulo','subtitulo','fecha','hora','categoria','imagen','cuerpo']

    



