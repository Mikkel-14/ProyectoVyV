# Generated by Django 4.0 on 2022-02-23 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0001_initial'),
        ('diagrama_gantt', '0003_tarea_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='proyecto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyectos.proyecto'),
        ),
        migrations.DeleteModel(
            name='Proyecto',
        ),
    ]
