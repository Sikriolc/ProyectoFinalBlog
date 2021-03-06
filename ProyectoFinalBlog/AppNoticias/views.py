from django.shortcuts import render,redirect
from django.contrib import messages
from django.db.models import Q
import datetime
from AppInterface.models import Categoria
from django.contrib.admin.views.decorators import staff_member_required
from .forms import *
from .urls import *



# Vista de Crud Noticia

def noticias (request):
  noticias=Noticia.objects.all()
  noti1 = noticias[len(noticias)-1]
  noti2 = noticias[len(noticias)-2]
  noti3 = noticias[len(noticias)-3]

  return render (request,"AppNoticias/noticias.html",{"noti1":noti1,"noti2":noti2,"noti3":noti3,"noticias":noticias})

def noticiasdetalle(request,id):
  noticias=Noticia.objects.get(id=id)
  return render(request,"AppNoticias/noticiasdetalle.html",{"noticias":noticias})

@staff_member_required
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


@staff_member_required
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

@staff_member_required
def noticia_eliminar(request,id):
  noticia = Noticia.objects.get(id=id)
  noticia.delete()
  messages.success(request, "Noticia Eliminada!")
  return redirect("noticias")

