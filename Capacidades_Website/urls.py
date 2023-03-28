"""Capacidades_Website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Capacidades_App.views import crearCapacidad, editarCapacidad, eliminarCapacidad
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include('Capacidades_App.urls')), #Para incluir las apps utilizadas en una App en especifico utilizamos este comando

    path('admin/', admin.site.urls),
    path('register/',user_views.register,name='register'), #Estructura nomobre que queremos dar en navegador + de down
    path('profile/',user_views.profile,name='profile'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    #path('editar_Capacidad/<int:ID_SGI>', editarCapacidad, name='editar_Capacidad'),
    #path('crear_Capacidad/', crearCapacidad,name='crear_Capacidad'),
    #path('eliminar_Capacidad/<int:ID_SGI>', eliminarCapacidad, name='eliminar_Capacidad'),
]
