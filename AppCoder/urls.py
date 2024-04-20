from django.urls import path
from . import views

urlpatterns = [
    path("",views.inicio, name="home"),
    path("ver_cursos", views.ver_cursos, name="cursos"),
    path("ver_profesores", views.ver_profesores, name="profesores"),
    path("ver_alumnos", views.ver_alumnos, name="alumnos"),
    

    path("alta_curso", views.curso_formulario),
    path("alta_profesor", views.profesor_formulario),
    path("alta_alumno", views.alumno_formulario),

    path("buscar_curso", views.buscar_curso),
    path("buscar_profesor", views.buscar_profesor ),
    path("buscar_alumno", views.buscar_alumno),

    path("buscardor_de_cursos", views.buscador_de_curso),
    path("buscardor_de_profesores", views.buscardor_de_profesores),
    path("buscardor_de_alumnos", views.buscardor_de_alumnos),

    path("editar_curso/<int:id>", views.editar_curso, name="editar_curso"),

    path("eliminar_curso/<int:id>" , views.eliminar_curso , name="eliminar_curso"), 

    path("modificar_curso/<int:id>" , views.modificar , name="modificar_curso"),

    path("login", views.login_request , name="login"),

    path("register" , views.register , name="register")
]
