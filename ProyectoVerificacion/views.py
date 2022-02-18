from .forms import BasicUserCreationForm
from django.shortcuts import render,redirect
from django.contrib.auth import logout


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