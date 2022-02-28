from .forms import BasicUserCreationForm
from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from proyectos.models import Proyecto, ProyectoUsuario


def register_view(request):
    form = BasicUserCreationForm()
    if request.method == 'POST':
        form = BasicUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')

    return render(request, 'registro_usuario.html', {'form': form})


def cerrar_sesion(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def acceso_proyecto_guard(request, id_proyecto):
    usuario = request.user
    proyecto = Proyecto.objects.get(id=id_proyecto)
    return proyecto in ProyectoUsuario.obtener_proyectos(usuario)