from django.urls import path
from . import views

urlpatterns = [
    path("",views.inicio, name="home"),
    path("ver_cursos", views.ver_cursos, name="cursos"),
    path("ver_profesores", views.profesores, name="profesores"),
    path("ver_alumnos", views.alumnos, name="alumnos"),
    

    path("alta_curso", views.curso_formulario),
    path("alta_profesor", views.profesor_formulario),
    path("alta_alumno", views.alumno_formulario),

    path("buscar_curso", views.buscar_curso),
    path("buscar_profesor", views.buscar_profesor ),
    path("buscar_alumno", views.buscar_alumno),

    path("buscar", views.buscar),
    path("buscardor_de_profesores", views.buscardor_de_profesores),
    path("buscardor_de_alumnos", views.buscardor_de_alumnos)
]
