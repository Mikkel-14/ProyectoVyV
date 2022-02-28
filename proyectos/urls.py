from django.urls import path, include
from . import views

urlpatterns = [
    path('nuevo', views.crear_proyecto, name='crearProyecto'),
    path('', views.acceso_proyectos_guard, name='verProyectos'),
    path('<int:id_proyecto>/eliminar', views.eliminar_proyecto, name='eliminarProyecto'),
    path('<int:id_proyecto>/gantt/', include('diagrama_gantt.urls')),
    path('<int:id_proyecto>/tareas/', include('tareas.urls')),
]