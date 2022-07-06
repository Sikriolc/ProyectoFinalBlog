from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NoticiaForm(forms.ModelForm):
  class Meta:
    model = Noticia
    fields = "__all__"



    



