from django.db import models
from django.contrib.auth.models import User


class Proyecto(models.Model):
    nombre_proyecto = models.CharField(max_length=100)
    usuarios = models.ManyToManyField(User, through='ProyectoUsuario')

    def agregar_colaborador(self, usuario):
        nueva_entrada = ProyectoUsuario(id_usuario = usuario, id_proyecto = self)
        nueva_entrada.save()


class ProyectoUsuario(models.Model):
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    id_proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    
    def obtener_proyectos(usuario):
        return list(usuario.proyecto_set.all())
    
    def tiene_proyectos(usuario):
        return len(ProyectoUsuario.obtener_proyectos(usuario)) > 0

    def crear_proyecto(nombre_proyecto, usuario):
        nuevo_proyecto = Proyecto(nombre_proyecto=nombre_proyecto)
        nuevo_proyecto.save()
        nuevo_proyecto.agregar_colaborador(usuario=usuario)
        return nuevo_proyecto
        
    def numero_colaboradores(id_proyecto):
        return ProyectoUsuario.objects.filter(id_proyecto=id_proyecto).count()