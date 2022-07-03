from django.shortcuts import render
from .models import *

# Create your views here.

def publicaciones(request):
    return render(request,'AppPublicaciones/publicaciones.html')