from behave import *
from django.contrib.auth.models import Permission, User
from proyectos.models import ProyectoUsuario
from django.shortcuts import redirect
from django.http import HttpRequest
from proyectos.views import acceso_proyectos_guard
use_step_matcher("re")


@step("que no existe ningún proyecto del administrador en el módulo de proyectos")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    # Se simula que un usuario con permisos va a iniciar sesión
    context.usuario = User.objects.create_user('testuser', 'testUser@verificacionyvalidacion.com',
                                            'VerificacionyValidaci0n')
    permiso = Permission.objects.get(codename='add_proyecto')
    context.usuario.user_permissions.add(permiso)
    context.usuario.save()
    # Verifica si existen proyectos
    assert not ProyectoUsuario.tiene_proyectos(context.usuario)


@step("el sistema redirigirá al administrador a la ventana de creación de nuevo proyecto")
def step_impl(context):
    expected  = redirect('crearProyecto').url
    request = HttpRequest()
    request.user = context.usuario
    actual = acceso_proyectos_guard(request).url
    assert expected == actual


@step("que el administrador tiene proyectos registrados")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    # Se simula que un usuario con permisos va a iniciar sesión
    context.usuario = User.objects.create_user('testuser', 'testUser@verificacionyvalidacion.com',
                                            'VerificacionyValidaci0n')
    permiso = Permission.objects.get(codename='add_proyecto')
    context.usuario.user_permissions.add(permiso)
    context.usuario.save()
    # Se crean proyecto de ejemplo
    proyecto1 = ProyectoUsuario.crear_proyecto(nombre_proyecto='Proyecto 1', usuario=context.usuario)
    proyecto2 = ProyectoUsuario.crear_proyecto(nombre_proyecto='Proyecto 2', usuario=context.usuario)
    proyecto3 = ProyectoUsuario.crear_proyecto(nombre_proyecto='Proyecto 3', usuario=context.usuario)
    proyecto4 = ProyectoUsuario.crear_proyecto(nombre_proyecto='Proyecto 4', usuario=context.usuario)
    context.proyectos = {proyecto1, proyecto2, proyecto3, proyecto4}


@step("se mostrará una lista de los proyectos existentes que le pertenecen al administrador")
def step_impl(context):
    actual = set(ProyectoUsuario.obtener_proyectos(context.usuario))
    assert actual == context.proyectos