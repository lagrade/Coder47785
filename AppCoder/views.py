from django.shortcuts import render, redirect
from AppCoder.models import Curso
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def crear_curso(request):
     curso = Curso(nombre ="javascript", camada=25132)
     curso.save()
     return redirect("/app/cursos/")



def show_html(request):
     curso = Curso.objects.first()
     contexto ={ "curso" : curso, "nombre": "Laura"}
     return  render(request, "index.html", contexto)

def mostrar_cursos(request):
     cursos = Curso.objects.all()
     contexto = {
          "cursos": cursos,
          "nombre": "laura"
     }
     return render(request, "AppCoder/cursos.html", contexto)