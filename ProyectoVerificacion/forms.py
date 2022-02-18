from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group


class BasicUserCreationForm(UserCreationForm):
    def save(self, commit=True):
        user = super().save(commit=False)
        grupo = Group.objects.get(name="miembro_proyecto")
        if commit:
            user.save()
            user.groups.add(grupo)
        return user
