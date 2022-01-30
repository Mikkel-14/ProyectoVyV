from django.urls import path

from . import views

urlpatterns = [
    path('', views.acceso_tareas_guard, name='gantt'),
]