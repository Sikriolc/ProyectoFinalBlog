from django import forms
from .models import *

class CategoriaForm(forms.ModelForm):
  class Meta:
    model = Categoria
    fields = "__all__"
