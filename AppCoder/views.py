from django.shortcuts import render
from AppCoder.models import Curso, Profesor, Alumno
from django.http import HttpResponse
from django.template import loader
from AppCoder.forms import Curso_formulario, Profesor_formulario, Alumno_formulario
from django.contrib.auth.forms import AuthenticationForm , UserChangeForm, UserCreationForm
from django.contrib.auth import login, authenticate
# Create your views here. 

def inicio(request):
    
    return render(request, "padre.html")

def cursos(request):
    return render(request, "buscar_curso.html")

def alumnos(request):
    return render(request, "alumno.html")

def ver_profesores(request):
    return render(request, "buscar_profesor.html")

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

## Editar ##
def editar_curso(request, id):
    curso = Curso.objects.get(id=id)
    dicc = {"curso": curso}
    plantilla = loader.get_template("curso.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

def editar_alumno(request, id):
    alumno = Alumno.objects.get(id=id)
    dicc = {"alumno": alumno}
    plantilla = loader.get_template("alumnos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

def editar_profesor(request, id):
    profesor = Profesor.objects.get(id=id)
    dicc = {"profesor": profesor}
    plantilla = loader.get_template("profesores.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento) 

### Modificar ###
def modificar_curso(request , id):
    curso = Curso.objects.get(id=id)
    if request.method == "POST":
        mi_formulario = Curso_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso.nombre = datos["nombre"]
            curso.camada = datos["camada"]
            curso.save()
            return render(request , "curso.html" , {"curso":curso})
    else:
        mi_formulario = Curso_formulario(initial={"nombre":curso.nombre , "camada":curso.camada})

    return render( request , "modificar_curso.html" , {"mi_formulario": mi_formulario , "curso":curso})

def modificar_alumno(request , id):
    alumno = Alumno.objects.get(id=id)

    if request.method == "POST":
        mi_formulario = Alumno_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            alumno.nombre = datos["nombre"]
            alumno.apellido = datos["apellido"]
            alumno.email = datos["email"]
            alumno.save()
            return render(request , "alumnos.html  " , {"alumno":alumno})
    else:
        mi_formulario = Alumno_formulario(initial={"nombre":alumno.nombre , "apellido":alumno.apellido , "email":alumno.email})

    return render( request , "modificar_alumno.html" , {"mi_formulario": mi_formulario , "alumno":alumno})

def modificar_profesor(request , id):
    profesor = Profesor.objects.get(id=id)

    if request.method == "POST":
        mi_formulario = Profesor_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            profesor.nombre = datos["nombre"]
            profesor.apellido = datos["apellido"]
            profesor.materia = datos["materia"]
            profesor.email = datos["email"]
            profesor.save()
            return render(request , "profesores.html" , {"profesor":profesor})
    else:
        mi_formulario = Profesor_formulario(initial={"nombre":profesor.nombre , "apellido":profesor.apellido , "materia":profesor.materia , "email":profesor.email})

    return render(request , "modificar_profesor.html" , {"mi_formulario": mi_formulario , "profesor":profesor})

### Eliminar ###

def eliminar_curso(request , id ):
    curso = Curso.objects.get(id=id)
    curso.delete()
    curso = Curso.objects.all()
    return render(request , "buscar_curso.html" , {"cursos":curso})
    
###login##
def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra =  form.cleaned_data.get("password")
            user = authenticate(username=usuario, password=contra)
            if user is not None:
                login(request , user)
                return render(request , "inicio.html" , {"mensaje":f"Bienvenido {usuario}"})

            else:
                return HttpResponse(f"Usuario no encontrado")
        else:
            return HttpResponse(f"FORM INCORRECTO {form}")

    form = AuthenticationForm()
    return render(request, "login.html" , {"form":form})

def register(request):
    if request.method == "POST":
        form =  UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Usuario creado")
    else:
        form = UserCreationForm()
    return render(request , "registro.html" , {"form":form})







        
