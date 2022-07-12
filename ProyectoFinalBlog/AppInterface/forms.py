from django import forms
from .models import Categoria, PlusUser
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
    email=forms.EmailField()
    password1=forms.CharField(label="Contraseña",widget=forms.PasswordInput)
    password2=forms.CharField(label="Confirmar Contraseña",widget=forms.PasswordInput)
    
    class Meta:
      model= User
      fields = ['email','password1','password2']
      help_texts={k:"" for k in fields}

class EditPlusUser(forms.Form):
  email=forms.EmailField()
  password1=forms.CharField(label="Contraseña",widget=forms.PasswordInput)
  password2=forms.CharField(label="Confirmar Contraseña",widget=forms.PasswordInput)
  nick_name=forms.CharField(max_length=20, required=False)
  fecha_nacimiento=forms.DateTimeField(required=False)
  foto_perfil=forms.ImageField(label="Imagen", required=False)
  biografia=forms.CharField(required=False)

  class Meta:
        model = PlusUser
        fields = ['email','password1','password2','nick_name','fecha_nacimiento','foto_perfil','biografia']



    



