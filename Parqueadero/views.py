# Importaciones necesarias
from django.shortcuts import render

# Funciones necesarias para el funcionamiento junto con el FrontEnd
from django.shortcuts import render
from .models import Parqueadero

def parqueadero(request):
    cantidad = Parqueadero.objects.count()
    return render(request, 'parqueadero.html', {'cantidad': cantidad})
