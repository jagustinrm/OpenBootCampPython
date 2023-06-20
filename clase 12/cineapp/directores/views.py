from django.shortcuts import render
from .models import Director

def lista_directores(request):
    directores = Director.objects.all()
    return render(request, 'directores/lista_directores.html', {'directores': directores})