from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.

def inicio(request):
    return render(request, "AppInterface/inicio.html",)

#---------------------------------------


def categorias(request):

  categorias= Categoria.objects.all()

  return render(request,"AppInterface/categorias.html",{"categorias":categorias})

def categorias_crear(request):

  formulario = CategoriaForm(request.POST,request.FILES or None)
  if formulario.is_valid():
    formulario.save()
    return redirect("categorias")

  return render (request,"AppInterface/categorias_crear.html",{"formulario":formulario})

def categorias_editar(request):

  return render(request,"AppInterface/categorias_editar.html")

#---------------------------------------

def nosotros(request):

  return render(request,"AppInterface/nosotros.html",)

#---------------------------------------

def contacto(request):

  return render(request,"AppInterface/contacto.html",)

