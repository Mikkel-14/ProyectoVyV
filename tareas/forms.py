from django import forms


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
    fecha_inicial = forms.DateField(label="Fecha de inicio",
                                    widget=forms.DateInput(
                                       attrs={
                                           'class': 'form-control',
                                           'id': 'fecha_inicial',
                                           'type': 'date'
                                       })
                                    )
    fecha_limite = forms.DateField(label="Fecha límite",
                                   widget=forms.DateInput(
                                       attrs={
                                           'class': 'form-control',
                                           'id': 'fecha_limite',
                                           'type': 'date'
                                       })
                                   )
