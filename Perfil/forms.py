from django import forms

class RegistroForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
    correo = forms.EmailField(label='Correo', max_length=254)
    contrasena = forms.CharField(label='Contraseña', widget=forms.PasswordInput(), max_length=50)
    tipo_vehiculo_choices = [('moto', 'Moto'), ('carro', 'Carro')]
    tipo_vehiculo = forms.ChoiceField(choices=tipo_vehiculo_choices, label='Tipo de Vehículo')
    combustible_choices = [('eléctrico', 'Eléctrico'), ('gasolina', 'Gasolina'), ('hibrido', 'Híbrido'), ('otros', 'Otros')]
    combustible = forms.ChoiceField(choices=combustible_choices, label='Combustible')


class VehiculoForm(forms.Form):
    modelo = forms.CharField(label='Modelo', max_length=50)
    tipo_vehiculo_choices = [('moto', 'Moto'), ('carro', 'Carro')]
    tipo_vehiculo = forms.ChoiceField(choices=tipo_vehiculo_choices, label='Tipo de Vehículo')
    combustible_choices = [('eléctrico', 'Eléctrico'), ('gasolina', 'Gasolina'), ('hibrido', 'Híbrido'), ('otros', 'Otros')]
    combustible = forms.ChoiceField(choices=combustible_choices, label='Combustible')
