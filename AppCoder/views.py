from django.shortcuts import render
from AppCoder.models import Curso, Profesor, Alumno
from django.http import HttpResponse
from django.template import loader
from AppCoder.forms import Curso_formulario, Profesor_formulario, Alumno_formulario
# Create your views here.

def inicio(request):
    return render(request, "padre.html")

def ver_cursos(request):
    return render(request, "curso_1.1.html")

def ver_profesores(request):
    return render(request, "profesor_1.1.html")

def ver_alumnos(request):
    return render(request, "alumno_1.1.html")

#def ver_cursos(request):
 #   cursos = Curso.objects.all()
  #  dicc = {"cursos": cursos}
  #  plantilla = loader.get_template("cursos.html")
  #  documento = plantilla.render(dicc)
  #  return HttpResponse(documento)

#def ver_profesores(request):
 #   profesores = Profesor.objects.all()
  #  dicc = {"profesores": profesores}
   # plantilla = loader.get_template("profesores.html")
    #documento = plantilla.render(dicc)
    #return HttpResponse(documento)

#def ver_alumnos(request):
 #   alumnos = Alumno.objects.all()
  #  dicc = {"alumnos": alumnos}
   # plantilla = loader.get_template("alumnos.html")
    #documento = plantilla.render(dicc)
    #return HttpResponse(documento)

def curso_formulario(request):

    if request.method == "POST":
        mi_formulario = Curso_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data #Limpia el formularo, es in dict
            curso = Curso(nombre=datos["nombre"], camada=datos["camada"])
            curso.save()
            return render(request, "formulario_curso.html")

    return render(request, "formulario_curso.html")

def profesor_formulario(request):

    if request.method == "POST":
        mi_formulario = Profesor_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data #Limpia el formularo, es in dict
            profesor = Profesor(nombre=datos["nombre"], apellido=datos["apellido"], materia=datos["materia"], email=datos["email"])
            profesor.save()
            return render(request, "formulario_profesor.html")

    return render(request, "formulario_profesor.html")

def alumno_formulario(request):

    if request.method == "POST":
        mi_formulario = Alumno_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data #Limpia el formularo, es in dict
            alumno = Alumno(nombre=datos["nombre"], apellido=datos["apellido"], email=datos["email"])
            alumno.save()
            return render(request, "formulario_alumno.html")

    return render(request, "formulario_alumno.html")
###### Busca un Curso #####
def buscar_curso(request):

    return render(request, "buscar_curso.html")

###### Busca un Profesor #####  
def buscar_profesor(request):

    return render(request, "buscar_profesor.html")
######Busca un Alumno #####  
def buscar_alumno(request):

    return render(request, "buscar_alumno.html")

def buscador_de_curso(request):

    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        cursos = Curso.objects.filter(nombre__icontains= nombre)
        return render(request, "resultado_busqueda_curso.html", {"cursos":cursos})

    else:
        return HttpResponse("Ingrese el nombre del curso")

def buscardor_de_profesores(request):

    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        profesores = Profesor.objects.filter(nombre__icontains= nombre)
        return render(request, "resultado_busqueda_profesor.html", {"profesores":profesores})

    else:
        return HttpResponse("Ingrese el nombre del Profesor")
    
def buscardor_de_alumnos(request):

    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        alumnos = Alumno.objects.filter(nombre__icontains= nombre)
        return render(request, "resultado_busqueda_alumno.html", {"alumnos":alumnos})

    else:
        return HttpResponse("Ingrese el nombre del Alumno")
        
