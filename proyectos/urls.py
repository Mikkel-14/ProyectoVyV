from django.urls import path
from . import views

urlpatterns = [
    path('nuevo',views.acceso_proyectos_guard,name='crearProyecto'),
    path('',views.acceso_proyectos_guard,name='verProyectos')
]