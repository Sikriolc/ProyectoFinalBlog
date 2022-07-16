from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.

def publicaciones(request):
  public=Publicacion.objects.all()
  return render(request,'AppPublicaciones/publicaciones.html',{"public":public})


def publicacion_crear(request):

  if request.method=='POST':
    PubliForm=PublicForm(request.POST or None,request.FILES or None)

    if PubliForm.is_valid():
      info=PubliForm.cleaned_data
      PublicacionNueva=Publicacion(titulo=info['titulo'],subtitulo=info['subtitulo'],fecha=info['fecha'],hora=info['hora'],imagen=info['imagen'],cuerpo=info['cuerpo'],autor=request.user)
      PublicacionNueva.save()
      return redirect("publicaciones")

  PubliForm=PublicForm()
  return render (request,"AppPublicaciones/publicaciones_crear.html",{"PubliForm":PubliForm})

def publicacion_editar(request):
  publi=User()
  autor=publi
#contexto

  try: 
    publi_crear=Publicacion.objects.get(autor)
  except:
    publi_crear=Publicacion()
    publi_crear.autor=publi

  if request.method == "POST":

    PubliForm=PublicForm(request.POST, request.FILES)

    if PubliForm.is_valid():

      info2=PubliForm.cleaned_data
      publi_crear.titulo=info2["titulo"]
      publi_crear.autor=info2["autor"]
      publi_crear.subtitulo=info2["subtitulo"]
      publi_crear.fecha=info2["fecha"]
      publi_crear.hora=info2["hora"]
      publi_crear.imagen=info2["imagen"]
      publi_crear.cuerpo=info2["cuerpo"]

      
      publi_crear.save()
      return redirect("inicio")

  else:

    PubliForm=PublicForm(initial={"titulo":publi_crear.titulo,
    "autor":publi_crear.autor,
    "subtitulo":publi_crear.subtitulo,
    "fecha":publi_crear.fecha,
    "hora":publi_crear.hora,
    "imagen":publi_crear.imagen,
    "cuerpo":publi_crear.cuerpo})

  return render(request,"AppPublicaciones/publicaciones_editar.html",{"PubliForm":PubliForm})