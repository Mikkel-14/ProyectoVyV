from django.urls import path

from . import views

urlpatterns = [
    path('nueva', views.crear_tarea, name='crearTarea'),
    path('<int:id_tarea>', views.ver_tarea, name='verTarea'),
    path('<int:id_tarea>/editar', views.editar_tarea, name='editarTarea'),
    path('<int:id_tarea>/eliminar', views.eliminar_tarea, name='eliminarTarea'),
]