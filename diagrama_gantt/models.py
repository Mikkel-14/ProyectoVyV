from django.db import models

class Proyecto(models.Model):
    nombre_proyecto = models.CharField(max_length=100)


class Estado(models.Model):
    nombre_estado = models.CharField(max_length=20)
    color_estado = models.CharField(max_length=9)


class Tarea(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    nombre_tarea = models.CharField(max_length=100)
    fecha_inicial = models.DateField()
    fecha_limite = models.DateField()
    esta_completado = models.BooleanField()