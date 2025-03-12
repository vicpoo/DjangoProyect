#Main/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Batalla, Comentario, SpiderMan, Enemigo, Universo
from .forms import BatallaForm
import requests
import json

def home(request):
    """
    Vista para la página de inicio.
    """
    return render(request, 'main/home.html')

@login_required
def batallas(request):
    """
    Vista para listar todas las batallas (requiere autenticación).
    """
    batallas = Batalla.objects.all()
    return render(request, 'main/batallas.html', {'batallas': batallas})

@login_required
def detalle_batalla(request, id):
    """
    Vista para mostrar los detalles de una batalla específica (requiere autenticación).
    """
    batalla = get_object_or_404(Batalla, id=id)
    comentarios = Comentario.objects.filter(batalla=batalla)
    return render(request, 'main/detalle_batalla.html', {'batalla': batalla, 'comentarios': comentarios})

def login_view(request):
    """
    Vista para manejar el inicio de sesión de usuarios.
    """
    if request.method == 'POST':
        # Usamos .get() para evitar KeyError si los campos no están presentes
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Autenticar al usuario
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Si las credenciales son correctas, iniciar sesión
            login(request, user)
            return redirect('home')  # Redirigir a la página de inicio
        else:
            # Si las credenciales son incorrectas, mostrar un mensaje de error
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    
    # Si no es una solicitud POST, mostrar el formulario de inicio de sesión
    return render(request, 'main/login.html')

def logout_view(request):
    """
    Vista para manejar el cierre de sesión de usuarios.
    """
    logout(request)
    return redirect('home')  # Redirigir a la página de inicio después de cerrar sesión

def registro(request):
    """
    Vista para manejar el registro de nuevos usuarios.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Guardar el nuevo usuario
            return redirect('login')  # Redirigir al formulario de inicio de sesión
    else:
        form = UserCreationForm()
    
    return render(request, 'main/registro.html', {'form': form})

@login_required
def nueva_batalla(request):
    """
    Vista para crear una nueva batalla (requiere autenticación).
    """
    if request.method == 'POST':
        form = BatallaForm(request.POST)
        if form.is_valid():
            form.save()  # Guardar la nueva batalla
            return redirect('batallas')  # Redirigir a la lista de batallas
    else:
        form = BatallaForm()
    
    return render(request, 'main/nueva_batalla.html', {'form': form})

@login_required
def editar_batalla(request, id):
    """
    Vista para editar una batalla existente (requiere autenticación).
    """
    batalla = get_object_or_404(Batalla, id=id)
    
    if request.method == 'POST':
        form = BatallaForm(request.POST, instance=batalla)
        if form.is_valid():
            form.save()  # Guardar los cambios
            return redirect('detalle_batalla', id=batalla.id)  # Redirigir a los detalles de la batalla
    else:
        form = BatallaForm(instance=batalla)
    
    return render(request, 'main/editar_batalla.html', {'form': form})

@login_required
def eliminar_batalla(request, id):
    """
    Vista para eliminar una batalla existente (requiere autenticación).
    """
    batalla = get_object_or_404(Batalla, id=id)
    batalla.delete()  # Eliminar la batalla
    return redirect('batallas')  # Redirigir a la lista de batallas

def about(request):
    """
    Vista para la página de about.
    """
    try:
        response = requests.get('http://10.10.0.43:8000/about/')
        response.raise_for_status()  # Lanza una excepción si la respuesta no es exitosa
        lista = response.json()
    except requests.exceptions.RequestException as e:
        lista = []
        messages.error(request, f"Error al obtener la lista: {e}")
    except json.JSONDecodeError as e:
        lista = []
        messages.error(request, f"Error al decodificar la respuesta JSON: {e}")

    return render(request, 'main/about.html', {'lista': lista})