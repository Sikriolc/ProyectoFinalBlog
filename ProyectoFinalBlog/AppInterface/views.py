from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth.forms import AuthenticationForm #, UserCreationForm
from django.contrib.auth import login,logout, authenticate 
# Create your views here.

def inicio(request):
    return render(request, "AppInterface/inicio.html",)

#---------------------------------------

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

def categorias_editar(request):

  return render(request,"AppInterface/categorias_editar.html")

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

