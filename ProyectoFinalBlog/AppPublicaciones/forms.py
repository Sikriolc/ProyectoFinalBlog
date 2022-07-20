from django import forms
from .models import *
from wsgiref.handlers import format_date_time
from django.forms.widgets import NumberInput
from ckeditor.widgets import CKEditorWidget


class PublicForm(forms.ModelForm):
  #autor=forms.CharField(max_length=100)
  titulo=forms.CharField(max_length=100)
  subtitulo=forms.CharField(max_length=100)
  fecha=forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
  hora=forms.TimeField(widget=NumberInput(attrs={'type': 'time'}))
  imagen=forms.ImageField(label="Imagen Noticia", required=False)
  #cuerpo=forms.CharField(max_length=1500, widget=forms.Textarea())

  class Meta:
        model = Publicacion
        fields = ['titulo','subtitulo','fecha','hora','imagen','cuerpo']