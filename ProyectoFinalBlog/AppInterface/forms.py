from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CategoriaForm(forms.ModelForm):
  class Meta:
    model = Categoria
    fields = "__all__"

class UserRegisterForm(UserCreationForm):

  email=forms.EmailField()
  password1=forms.CharField(label="Contraseña",widget=forms.PasswordInput)
  password2=forms.CharField(label="Confirmar Contraseña",widget=forms.PasswordInput)
  image= forms.ImageField(required=False)

  class Meta:
    model= User
    fields= ['username','email','password1','password2']
    help_texts={k:"" for k in fields}

class UserEditForm(UserCreationForm):
    fecha_nacimiento=forms.DateField()
    nick_name=forms.CharField(max_length=20)
    email=forms.EmailField()
    password1=forms.CharField(label="Contraseña",widget=forms.PasswordInput)
    password2=forms.CharField(label="Confirmar Contraseña",widget=forms.PasswordInput)
    biografia=forms.CharField()
    
    class Meta:
      model= User
      fields = ['email','password1','password2']
      help_texts={k:"" for k in fields}



    



