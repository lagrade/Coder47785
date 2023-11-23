from django.shortcuts import render, redirect
from AppCoder.models import Curso
from AppCoder.form import CursoForm, BusquedaCursoForm
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def crear_curso(request):
     curso = Curso(nombre ="javascript", camada=25132)
     curso.save()
     return redirect("/app/cursos/")

def crear_curso_form (request):
     if request.method == "POST":
          curso_formulario =CursoForm(request.POST)
          if curso_formulario.is_valid():
               informacion =curso_formulario.cleaned_data

          curso_crear = Curso(nombre=informacion["nombre"], camada=informacion ["camada"])
          curso_crear.save()

          return redirect("/app/curso/")
     curso_formulario = Curso.objects.all()
     contexto = {
          "form": curso_formulario
     }
     return render(request, "AppCoder/crearcurso.html", contexto)

def Busqueda_camada(request):
     nombre= request.GET["nombre"]
     curso= Curso.objects.filter(nombre_icontains= nombre)
def show_html(request):
     curso = Curso.objects.first()
     contexto ={ "curso" : curso, "nombre": "Laura"}
     return  render(request, "index.html", contexto)

def mostrar_cursos(request):
     cursos = Curso.objects.all()
     contexto = {
          "cursos": cursos,
          "nombre": "laura",
          "form": BusquedaCursoForm(),
     }
     return render(request, "AppCoder/cursos.html", contexto)