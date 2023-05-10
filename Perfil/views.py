# Importaciones necesarias
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from .forms import RegistroForm, VehiculoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuario
User = get_user_model()

# Funciones necesarias para el funcionamiento junto con el FrontEnd
def login_usuario(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = "Invalid username or password"
    else:
        error_message = None
    return render(request, 'login.html', {'error_message': error_message})




def registro_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            if Usuario.objects.filter(nombre=username).exists():
                messages.error(request, 'El nombre de usuario ya está en uso')
                return redirect('registro_usuario')
            else:
                if email.endswith('@eafit.edu.co'):
                    usuario = Usuario.objects.create(nombre=username, correo=email, contrasena=password1)
                    usuario.save()
                    usuario.idUsuario = usuario.pk
                    usuario.save()
                    # Inicia sesión al usuario automáticamente después del registro
                    usuario = authenticate(request, username=username, password=password1)
                    login(request, usuario)
                    messages.success(request, 'Registro completado exitosamente')
                    return redirect('vehiculo')
                else:
                    messages.error(request, 'El correo electrónico no es institucional')
                    return redirect('registro_usuario')
        else:
            messages.error(request, 'Las contraseñas no coinciden')
            return redirect('registro_usuario')
    return render(request, 'registro.html')



def dashboard_usuario(request):
    # Obtener el usuario actual desde la base de datos
    #user = Usuario.objects.get(pk=request.user.pk)

    # Renderizar la plantilla con la información del usuario
    return render(request, 'dashboard.html')


def logout_usuario(request):
    logout(request)
    messages.success(request, 'Sesión cerrada exitosamente')
    return redirect('login_usuario')


def index(request):
    return render(request, 'index.html')


def vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            vehiculo = form.save(commit=False)
            vehiculo.idUsuario = request.user.usuario
            vehiculo.save()
            return redirect('home')
    else:
        form = VehiculoForm()
    return render(request, 'vehiculo.html', {'form': form})


def about(request):
    return render(request, 'about.html')

def parkify(request):
    return render(request, 'parkify.html')



