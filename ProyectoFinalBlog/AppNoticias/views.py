from django.shortcuts import render,redirect
from django.contrib import messages
from django.db.models import Q
import datetime
from AppInterface.models import Categoria
from .forms import *
from .urls import *



# Create your views here.

def noticias(request):
  noticias=Noticia.objects.all()
  return render(request,"AppNoticias/noticias.html",{"noticias":noticias})

def noticia_crear(request):
  noti=Categoria()
  categoria=noti
  if request.method=='POST':
    NotiForm=NoticiaForm(request.POST or None,request.FILES or None)

    if NotiForm.is_valid():
      info=NotiForm.cleaned_data
      NoticiaNueva=Noticia(
      autor=request.user,
      titulo=info['titulo'],
      subtitulo=info['subtitulo'],
      fecha=info['fecha'],
      hora=info['hora'],
      categoria=info['categoria'],
      imagen=info['imagen'],
      cuerpo=info['cuerpo'],
      )
      NoticiaNueva.save()
      messages.success(request, "Noticia Creada!")
      return redirect("noticias")

  NotiForm=NoticiaForm()
  return render (request,"AppNoticias/noticias_crear.html",{"NotiForm":NotiForm})



def noticia_editar(request,id):
  noticia=Noticia.objects.get(id=id)
  noti=Categoria()
  categoria=noti
#contexto

  try: 
    noti_crear=Noticia.objects.get(categoria)
  except:
    noti_crear=Noticia()
    noti_crear.categoria=noti

  if request.method == "POST":

    NotiForm=NoticiaForm(request.POST, request.FILES, instance=noticia)

    if NotiForm.is_valid():

      info2=NotiForm.cleaned_data
      noticia.titulo=info2["titulo"]
      #noticia.autor=info2["autor"]
      noticia.subtitulo=info2["subtitulo"]
      noticia.fecha=info2["fecha"]
      noticia.hora=info2["hora"]
      noticia.imagen=info2["imagen"]
      noticia.categoria=info2["categoria"]
      noticia.cuerpo=info2["cuerpo"]

      messages.success(request, "Noticia Editada!")
      noticia.save()
      return redirect("noticias")

  else:

    NotiForm=NoticiaForm(initial=
      {"titulo":noticia.titulo,
      #"autor":noticia.autor,
      "subtitulo":noticia.subtitulo,
      "fecha":noticia.fecha,
      "hora":noticia.hora,
      "imagen":noticia.imagen,
      "categoria":noticia.categoria,
      "cuerpo":noticia.cuerpo})

  return render(request,"AppNoticias/noticias_editar.html",{"NotiForm":NotiForm})

def noticia_buscar(request):
  
  if request.method=='POST':
    titulos=request.POST["titulo"]
    Titu=Noticia.objects.filter( Q(titulo__icontains=titulos) | Q(cuerpo__icontains=titulos)).values()
    return render(request,"AppNoticias/noticia_buscar.html",{'Titu':Titu})
  
  else:

    Titu=[]
    return render(request,"AppNoticias/noticia_buscar.html",{'Titu':Titu})

def noticia_eliminar(request,id):
  noticia = Noticia.objects.get(id=id)
  noticia.delete()
  return redirect("noticias")

