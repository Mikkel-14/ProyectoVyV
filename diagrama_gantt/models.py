from django.db import models
from datetime import datetime


class Proyecto(models.Model):
    nombre_proyecto = models.CharField(max_length=100)

    def tiene_tareas(self):
        return Tarea.objects.filter(proyecto=self.id).count() > 0


class Estado(models.Model):
    nombre_estado = models.CharField(max_length=20)
    color_estado = models.CharField(max_length=9)


class Tarea(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    nombre_tarea = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500, blank=True, null=True)
    fecha_inicial = models.DateField()
    fecha_limite = models.DateField()
    esta_completado = models.BooleanField()

    def es_critica(self, fecha_actual=datetime.now().date()):
        tiempo_restante = self.fecha_limite - fecha_actual
        return (0 <= tiempo_restante.days <= 7) and not self.esta_completado

    def obtener_estado(self, fecha_actual=datetime.now().date()):
        if self.esta_completado:
            return 'completado'
        elif fecha_actual < self.fecha_inicial:
            return 'pendiente'
        elif self.es_critica(fecha_actual):
            return 'crítico'
        elif fecha_actual > self.fecha_limite:
            return 'atrasado'
        else:
            return 'en-progreso'

    def obtener_color(self, fecha_actual=datetime.now().date()):
        return Estado.objects.get(nombre_estado=self.obtener_estado(fecha_actual)).color_estado
