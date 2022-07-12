import re
from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth.forms import AuthenticationForm #, UserCreationForm
from django.contrib.auth import login,logout, authenticate 
from AppNoticias.models import *
# Create your views here.

def inicio(request):
  categorias=Categoria.objects.all()[0:2]
  return render(request, "AppInterface/inicio.html",{"categorias":categorias})

#---------------------------------------
def perfil(request):
    user=User.objects.all()
    return render(request, "AppInterface/perfil.html",{"user":user})

def login_request(request):
  if request.method=="POST":
    form=AuthenticationForm(request, data=request.POST)

    if form.is_valid():
      username = form.cleaned_data.get('username')
      password= form.cleaned_data.get('password')
      user=authenticate(username=username, password=password)
      
      if user is not None:
        login(request, user)
        return redirect("inicio")
      else:
        return redirect("login")
    return redirect("login")
  form= AuthenticationForm()

  return render(request,"AppInterface/login.html",{"form":form})

def logout_request(request):
  logout(request)
  return redirect("inicio")


def register_request(request):
  if request.method=="POST":
    form=UserRegisterForm(request.POST)

    if form.is_valid():
      username = form.cleaned_data.get('username')
      password= form.cleaned_data.get('password1')

      form.save()
      user=authenticate(username=username, password=password)


      return redirect("inicio")
    return render(request,"AppInterface/register.html",{"form":form})

  form=UserRegisterForm()
  return render(request,"AppInterface/register.html",{"form":form})

def editar_perfil(request):

  user = request.user

  if request.method == "POST":
    form= UserEditForm(request.POST)
    if form.is_valid():
      info=form.cleaned_data
      user.email=info["email"]
      user.password1=info["password1"]

      user.save()

      return redirect("inicio")
  else:

    form = UserEditForm(initial={"email":user.email})

  return render(request,"AppInterface/editarperfil.html",{"form":form})

def editar_PlusUser(request):
  plus = request.user

  if request.method == "POST":

    PlusForm=EditPlusUser(request.POST, request.FILES)

    if PlusForm.is_valid():

      info2=PlusForm.cleaned_data
      plus.email=info2["email"]
      plus.password1=info2["password1"]
      plus.password2=info2["password2"]
      plus.nick_name=info2["nick_name"]
      plus.fecha_nacimiento=info2["fecha_nacimiento"]
      plus.foto_perfil=info2["foto_perfil"]
      plus.biografia=info2["biografia"]
      plus.save()
      return redirect("inicio")

  else:

    PlusForm=EditPlusUser(initial={"email":plus.email})

  return render(request,"AppInterface/editarperfil.html",{"PlusForm":PlusForm})

def perfil(request):
  #form = User.objects.all()
  plus= PlusUser.objects.all()

  return render(request,"AppInterface/perfil.html",{"plus":plus})


#---------------------------------------
def categorias(request):

  categorias= Categoria.objects.all()

  return render(request,"AppInterface/categorias.html",{"categorias":categorias})

def categorias_crear(request):

  formulario = CategoriaForm(request.POST or None,request.FILES or None)
  if formulario.is_valid():
    formulario.save()
    return redirect("categorias")

  return render (request,"AppInterface/categorias_crear.html",{"formulario":formulario})

def categorias_editar(request,id):
  categoria= Categoria.objects.get(id=id)
  formulario = CategoriaForm(request.POST or None,request.FILES or None,instance=categoria)
  if formulario.is_valid() and request.POST:
    formulario.save()
    return redirect("categorias")
  return render (request,"AppInterface/categorias_editar.html",{"formulario":formulario})

def categorias_eliminar(request,id):
  categoria = Categoria.objects.get(id=id)
  categoria.delete()
  return redirect("categorias")

#---------------------------------------

def nosotros(request):

  return render(request,"AppInterface/nosotros.html",)

#---------------------------------------

def contacto(request):

  return render(request,"AppInterface/contacto.html",)

