# Generated by Django 4.0 on 2022-01-10 22:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_estado', models.CharField(max_length=20)),
                ('color_estado', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_proyecto', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_tarea', models.CharField(max_length=100)),
                ('fecha_inicial', models.DateField()),
                ('fecha_limite', models.DateField()),
                ('esta_completado', models.BooleanField()),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='diagrama_gantt.estado')),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diagrama_gantt.proyecto')),
            ],
        ),
    ]
