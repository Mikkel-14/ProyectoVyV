from django.db import models


class Proyecto(models.Model):
    nombre_proyecto = models.CharField(max_length=100)