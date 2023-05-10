# Importaciones necesarias
from django.db import models


class Error(models.Model):
    idError = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(auto_now_add=True)
    infoError = models.CharField(max_length=200)

    def informaErrorMec(self):
        # Se guarda el error en la base de datos
        self.save()

class Parqueadero(models.Model):
    ubicacion = models.CharField(max_length=50)
    capacidad = models.IntegerField(default=0)
    errores = models.ManyToManyField(Error)

    def modificaCapacidad(self, capacidadNueva):
        # Se modifica la capacidad del parqueadero
        self.capacidad = capacidadNueva
        self.save()

class Celda(models.Model):
    ubicacionCelda = models.CharField(max_length=50)
    tipoVehiculo = models.CharField(max_length=20)

    def ingresaTipoCelda(self, tipo):
        # Se asigna el tipo de celda según el tipo de vehículo
        if tipo == "discapacitados":
            self.tipoVehiculo = "Discapacitados"
        elif tipo == "hibridos":
            self.tipoVehiculo = "Carros Híbridos"
        elif tipo == "electricos":
            self.tipoVehiculo = "Carros Eléctricos"
        else:
            self.tipoVehiculo = "Carros Normales"
        self.save()
