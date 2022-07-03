from django.shortcuts import render

# Create your views here.

def publicaciones(request):
    return render(request,'AppPublicaciones/publicaciones.html')