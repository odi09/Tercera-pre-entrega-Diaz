from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("",views.inicio, name="home"),
    path("cursos", views.cursos, name="cursos"),
    path("alumnos", views.alumnos, name="alumnos"),
    path("ver_profesores", views.ver_profesores, name="profesores"),
    
    

    path("alta_curso", views.curso_formulario),
    path("alta_profesor", views.profesor_formulario),
    path("alta_alumno", views.alumno_formulario),

    path("buscar_profesor", views.buscar_profesor ),
    path("buscar_alumno", views.buscar_alumno),

    path("buscardor_de_cursos", views.buscador_de_curso),
    path("buscardor_de_profesores", views.buscardor_de_profesores),
    path("buscardor_de_alumnos", views.buscardor_de_alumnos),

    path("editar_curso/<int:id>", views.editar_curso, name="editar_curso"),
    path("editar_alumno/<int:id>", views.editar_alumno, name="editar_alumno"),
    path("editar_profesor/<int:id>", views.editar_profesor, name="editar_profesor"),

    path("eliminar_curso/<int:id>" , views.eliminar_curso , name="eliminar_curso"), 

    path("modificar_curso/<int:id>" , views.modificar_curso , name="modificar_curso"),
    path("modificar_alumno/<int:id>" , views.modificar_alumno , name="modificar_alumno"),
    path("modificar_profesor/<int:id>" , views.modificar_profesor , name="modificar_profesor"),

    path("login", views.login_request , name="login"),

    path("register" , views.register , name="register"),
    path("logout" , LogoutView.as_view(template_name="logout.httml"), name="logout")
]
