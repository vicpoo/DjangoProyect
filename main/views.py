from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Batalla, Comentario

def home(request):
    return render(request, 'main/home.html')

def batallas(request):
    batallas = Batalla.objects.all()
    return render(request, 'main/batallas.html', {'batallas': batallas})

def detalle_batalla(request, id):
    batalla = get_object_or_404(Batalla, id=id)
    comentarios = Comentario.objects.filter(batalla=batalla)
    return render(request, 'main/detalle_batalla.html', {'batalla': batalla, 'comentarios': comentarios})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'main/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'main/registro.html', {'form': form})