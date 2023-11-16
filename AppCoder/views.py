from django.shortcuts import render
from AppCoder.models import Curso
from django.http import HttpResponse

# Create your views here.
def crear_curso(request):
     curso = Curso(nombre ="python", camada=47785)
     curso.save()
     contexto = {"curso": curso}

     return HttpResponse(f" su curso es {curso.nombre} y la camada es {curso.camada}")

def show_html(request):
     curso = Curso.objects.first()
     contexto ={ "curso" : curso, "nombre": "Laura"}
     return  render(request, "index.html", contexto)