from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q


# Create your views here.
@login_required
def publicaciones(request):
  public=Publicacion.objects.all()
  return render(request,'AppPublicaciones/publicaciones.html',{"public":public})


@login_required
def publicacion_crear(request):

  if request.method=='POST':
    PubliForm=PublicForm(request.POST or None,request.FILES or None)

    if PubliForm.is_valid():
      info=PubliForm.cleaned_data
      PublicacionNueva=Publicacion(titulo=info['titulo'],subtitulo=info['subtitulo'],fecha=info['fecha'],hora=info['hora'],imagen=info['imagen'],cuerpo=info['cuerpo'],autor=request.user)
      PublicacionNueva.save()
      messages.success(request, "Publicacion Creada!")
      return redirect("publicaciones")

  PubliForm=PublicForm()
  return render (request,"AppPublicaciones/publicaciones_crear.html",{"PubliForm":PubliForm})

@login_required
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
      #publicacion.autor=info2["autor"]
      publicacion.subtitulo=info2["subtitulo"]
      publicacion.fecha=info2["fecha"]
      publicacion.hora=info2["hora"]
      publicacion.imagen=info2["imagen"]
      publicacion.cuerpo=info2["cuerpo"]

      
      publicacion.save()
      messages.success(request, "Publicacion Editada con Exito!")
      return redirect("inicio")

  else:

    PubliForm=PublicForm(initial={"titulo":publicacion.titulo,
    #"autor":publicacion.autor,
    "subtitulo":publicacion.subtitulo,
    "fecha":publicacion.fecha,
    "hora":publicacion.hora,
    "imagen":publicacion.imagen,
    "cuerpo":publicacion.cuerpo})

  return render(request,"AppPublicaciones/publicaciones_editar.html",{"PubliForm":PubliForm})

@login_required
def publicacion_buscar(request):
  
  if request.method=='POST':
    titulos=request.POST["titulo"]
    Titu=Publicacion.objects.filter( Q(titulo__icontains=titulos) | Q(cuerpo__icontains=titulos)).values()
    return render(request,"AppPublicaciones/publicaciones_buscar.html",{'Titu':Titu})
  
  else:

    Titu=[]
    return render(request,"AppPublicaciones/publicaciones_buscar.html",{'Titu':Titu})

def publicacion_eliminar(request,id):
  publicacion = Publicacion.objects.get(id=id)
  publicacion.delete()
  messages.success(request, "Publicacion eliminada correctamente!")
  return redirect("publicaciones")