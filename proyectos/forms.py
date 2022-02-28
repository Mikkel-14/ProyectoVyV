from django import forms
from django.contrib.auth.models import User


class IngresoProyecto(forms.Form):
    OPTIONS = tuple([
                    (usuario.id, usuario.username)
                    for usuario in User.objects.all()
                    if usuario.groups.filter(name='miembro_proyecto').exists()
                ])
    nombre_proyecto = forms.CharField(max_length=250, label="Nombre del proyecto:",
                                      widget=forms.TextInput(
                                          attrs={
                                              'class': 'form-control',
                                              'id': 'nombre',
                                              'placeholder': 'Nombre del proyecto'
                                          }
                                      ))
    colaboradores_proyecto = forms.MultipleChoiceField(widget=forms.widgets.SelectMultiple(
                                                        attrs={
                                                            'class': "form-select"
                                                        }),
                                                       choices=OPTIONS
                                                    )
