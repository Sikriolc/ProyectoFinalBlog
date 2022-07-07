from django.shortcuts import render,redirect
import datetime
from AppInterface.models import Categoria
from .forms import *

# Create your views here.

def noticias(request):
    return render(request,'AppNoticias/noticias.html')


def noticia_crear(request):
  categorias=Categoria.objects.all()
  formulario = NoticiaForm(request.POST or None,request.FILES or None)
  if formulario.is_valid():
    formulario.save()
    return redirect("categorias")

  return render (request,"AppNoticias/noticias_crear.html",{"formulario":formulario,"categorias":categorias},)