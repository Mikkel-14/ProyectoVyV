from django import forms
from datetime import datetime, timedelta


class IngresoTarea(forms.Form):
    nombre_tarea = forms.CharField(max_length=100, label="Nombre de la tarea:",
                                   widget=forms.TextInput(
                                       attrs={
                                           'class': 'form-control',
                                           'id': 'nombre',
                                           'placeholder': 'Nombre de la tarea'
                                       }
                                   ))
    descripcion = forms.CharField(max_length=500, label="Descipción",
                                  widget=forms.Textarea(
                                      attrs={
                                          'class': 'form-control',
                                          'id': 'descipcion',
                                          'rows': 3,
                                          'placeholder': 'Descripción'
                                      }
                                  ))
    fecha_inicio = forms.DateField(label="Fecha de inicio",
                                   widget=forms.DateInput(
                                       attrs={
                                           'class': 'form-control',
                                           'id': 'fecha_inicial',
                                           'min': datetime.today().date().strftime('%Y-%m-%d'),
                                           'type': 'date'
                                       })
                                   )
    fecha_limite = forms.DateField(label="Fecha límite",
                                   widget=forms.DateInput(
                                       attrs={
                                           'class': 'form-control',
                                           'id': 'fecha_limite',
                                           'min': (datetime.today() + timedelta(days=1)).date().strftime('%Y-%m-%d'),
                                           'type': 'date'
                                       })
                                   )
