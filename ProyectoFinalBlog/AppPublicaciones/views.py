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

def publicacion_editar(request,id):
  publicacion=Publicacion.objects.get(id=id)
  publi=User()
  autor=publi
#contexto

  try: 
    publi_crear=Publicacion.objects.get(autor)
  except:
    publi_crear=Publicacion()
    publi_crear.autor=publi

  if request.method == "POST":

    PubliForm=PublicForm(request.POST or None, request.FILES or None, instance=publicacion)

    if PubliForm.is_valid():

      info2=PubliForm.cleaned_data
      publicacion.titulo=info2["titulo"]
      publicacion.autor=info2["autor"]
      publicacion.subtitulo=info2["subtitulo"]
      publicacion.fecha=info2["fecha"]
      publicacion.hora=info2["hora"]
      publicacion.imagen=info2["imagen"]
      publicacion.cuerpo=info2["cuerpo"]

      
      publicacion.save()
      return redirect("inicio")

  else:

    PubliForm=PublicForm(initial={"titulo":publicacion.titulo,
    "autor":publicacion.autor,
    "subtitulo":publicacion.subtitulo,
    "fecha":publicacion.fecha,
    "hora":publicacion.hora,
    "imagen":publicacion.imagen,
    "cuerpo":publicacion.cuerpo})

  return render(request,"AppPublicaciones/publicaciones_editar.html",{"PubliForm":PubliForm})

def publicacion_eliminar(request,id):
  publicacion = Publicacion.objects.get(id=id)
  publicacion.delete()
  return redirect("publicaciones")