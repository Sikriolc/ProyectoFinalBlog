from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, "AppInterface/inicio.html",)

#---------------------------------------


def categorias(request):

  return render(request,"AppInterface/categorias.html",)

def categorias_crear(request):

  return render(request,"AppInterface/categorias_crear.html")

def categorias_editar(request):

  return render(request,"AppInterface/categorias_editar.html")

#---------------------------------------

def nosotros(request):

  return render(request,"AppInterface/nosotros.html",)

#---------------------------------------

def contacto(request):

  return render(request,"AppInterface/contacto.html",)

