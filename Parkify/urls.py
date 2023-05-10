# Importaciones necesarias
from django.urls import path
from django.contrib.auth import views as auth_views
from Parqueadero.views import parqueadero
from Perfil.views import login_usuario,registro_usuario,dashboard_usuario,logout_usuario, index, vehiculo, about, parkify
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('', index, name='index'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login_usuario'),
    path('registro/', registro_usuario, name='registro_usuario'),
    path('dashboard/', dashboard_usuario, name='dashboard_usuario'),
    path('logout/', logout_usuario, name='logout_usuario'),
    path('vehiculo/', vehiculo, name='vehiculo'),
    path('about/', about, name='about'),
    path('parkify/', parkify, name='parkify'),
    path('parqueadero/', parqueadero, name='parqueadero'),
]

