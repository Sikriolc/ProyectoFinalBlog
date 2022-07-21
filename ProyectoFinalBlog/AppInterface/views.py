import re
from django.http import Http404
from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth.forms import AuthenticationForm #, UserCreationForm
from django.contrib.auth import login,logout, authenticate 
from AppNoticias.models import *
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Q


# Create your views here.

def inicio(request):
  user=request.user
  noticias=Noticia.objects.all()

  page = request.GET.get('page',1)

  try:
    paginator = Paginator(noticias,4)
    noticias =paginator.page(page)
  except:
    raise Http404
  
  #PlusForm=PlusUser.objects.get(usuario=user) ,"PlusForm":PlusForm

  return render(request, "AppInterface/inicio.html",{"entity":noticias,"paginator":paginator})

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
      messages.success(request, "Registrado con Exito!")

      if user is not None:
        login(request, user)
        return redirect("inicio")
      else:
        return redirect("login")

      #return redirect("inicio")
    return render(request,"AppInterface/register.html",{"form":form})

  form=UserRegisterForm()
  return render(request,"AppInterface/register.html",{"form":form})

@login_required
def editar_PlusUser(request):
  user = request.user

  try: 
    plus_user=PlusUser.objects.get(usuario=user)
  except:
    plus_user=PlusUser()
    plus_user.usuario=user
    plus_user.save()

  if request.method == "POST":

    PlusForm=EditPlusUser(request.POST, request.FILES)

    if PlusForm.is_valid():

      info2=PlusForm.cleaned_data
      user.email=info2["email"]
      #user.password1=info2["password1"]
      #user.password2=info2["password2"]
      plus_user.nick_name=info2["nick_name"]
      plus_user.fecha_nacimiento=info2["fecha_nacimiento"]
      plus_user.foto_perfil=info2["foto_perfil"]
      plus_user.biografia=info2["biografia"]

      user.save()
      plus_user.save()
      messages.success(request, "Editado a la Perfeccion querido Gamer!!")
      return redirect("inicio")

  else:

    PlusForm=EditPlusUser(initial={"email":user.email,"nick_name":plus_user.nick_name,"fecha_nacimiento":plus_user.fecha_nacimiento,"foto_perfil":plus_user.foto_perfil,"biografia":plus_user.biografia,})

  return render(request,"AppInterface/editarperfil.html",{"formulario":PlusForm})

@login_required
def perfil(request):
  user = request.user
  
  try: 
    plus_user=PlusUser.objects.get(usuario=user)
  except:
    plus_user=PlusUser()
    plus_user.usuario=user
    plus_user.save()

  return render(request,"AppInterface/perfil.html",{"PlusForm":plus_user})


#---------------------------------------
def categorias(request):

  categorias= Categoria.objects.all()
  page = request.GET.get('page',1)

  try:
    paginator = Paginator(categorias,2)
    categorias =paginator.page(page)
  except:
    raise Http404 

  return render(request,"AppInterface/categorias.html",{"entity":categorias,"paginator":paginator})

@staff_member_required
def categorias_crear(request):

  formulario = CategoriaForm(request.POST or None,request.FILES or None)
  if formulario.is_valid():
    formulario.save()
    messages.success(request, "Categoria Creada!")
    return redirect("categorias")

  return render (request,"AppInterface/categorias_crear.html",{"formulario":formulario})

@staff_member_required
def categorias_editar(request,id):
  categoria= Categoria.objects.get(id=id)
  formulario = CategoriaForm(request.POST or None,request.FILES or None,instance=categoria)
  if formulario.is_valid() and request.POST:
    formulario.save()
    messages.success(request, "Categoria editada con Exito!")
    return redirect("categorias")
  return render (request,"AppInterface/categorias_editar.html",{"formulario":formulario})

def categoria_buscar(request):
  
  if request.method=='POST':
    titulos=request.POST["titulo"]
    Titu=Categoria.objects.filter( Q(titulo__icontains=titulos) | Q(detalle__icontains=titulos)).values()
    return render(request,"AppInterface/categorias_buscar.html",{'Titu':Titu})
  
  else:

    Titu=[]
    return render(request,"AppInterface/categorias_buscar.html",{'Titu':Titu})

@staff_member_required
def categorias_eliminar(request,id):
  categoria = Categoria.objects.get(id=id)
  categoria.delete()
  messages.success(request, "Categoria eliminada correctamente!")
  return redirect("categorias")

#---------------------------------------

def nosotros(request):

  return render(request,"AppInterface/nosotros.html",)

#---------------------------------------
@login_required
def contacto(request):

  return render(request,"AppInterface/contacto.html",)

