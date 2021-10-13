from django.shortcuts import render
from .models import Curso

def index(request):
    dados = Curso.objects.all()
    return render(request,'home/index.html', {'dados':dados})
