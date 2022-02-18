from .forms import BasicUserCreationForm
from django.shortcuts import render,redirect


def register_view(request):
    form = BasicUserCreationForm()
    if request.method == 'POST':
        form = BasicUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')

    return render(request, 'registro_usuario.html', {'form': form})
