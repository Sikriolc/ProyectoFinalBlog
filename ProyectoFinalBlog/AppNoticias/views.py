from django.shortcuts import render,redirect
import datetime
from AppInterface.models import Categoria
from django.db.models import Q
from .forms import *

# Create your views here.

def noticias(request):
  noticias=Noticia.objects.all()
  return render(request,"AppNoticias/noticias.html",{"noticias":noticias})



def noticia_crear(request):
  noti=Categoria()
  categoria=noti
#contexto

  try: 
    noti_crear=Noticia.objects.get(categoria)
  except:
    noti_crear=Noticia()
    noti_crear.categoria=noti

  if request.method == "POST":

    NotiForm=NoticiaForm(request.POST, request.FILES)

    if NotiForm.is_valid():

      info2=NotiForm.cleaned_data
      noti_crear.titulo=info2["titulo"]
      noti_crear.autor=info2["autor"]
      noti_crear.subtitulo=info2["subtitulo"]
      noti_crear.fecha=info2["fecha"]
      noti_crear.hora=info2["hora"]
      noti_crear.imagen=info2["imagen"]
      noti_crear.categoria=info2["categoria"]
      noti_crear.cuerpo=info2["cuerpo"]

      
      noti_crear.save()
      return redirect("inicio")

  else:

    NotiForm=NoticiaForm(initial={"titulo":noti_crear.titulo,
    "autor":noti_crear.autor,
    "subtitulo":noti_crear.subtitulo,
    "fecha":noti_crear.fecha,
    "hora":noti_crear.hora,
    "imagen":noti_crear.imagen,
    "categoria":noti_crear.categoria,
    "cuerpo":noti_crear.cuerpo})

  return render(request,"AppNoticias/noticias_crear.html",{"NotiForm":NotiForm})

def noticia_buscar(request):
  
  if request.method=='POST':
    titulos=request.POST["titulo"]
    Titu=Noticia.objects.filter( Q(titulo__icontains=titulos) | Q(cuerpo__icontains=titulos)).values()
    return render(request,"AppNoticias/noticia_buscar.html",{'Titu':Titu})
  
  else:

    Titu=[]
    return render(request,"AppNoticias/noticia_buscar.html",{'Titu':Titu})
