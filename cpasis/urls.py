"""
URL configuration for cpasis project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from cpasisApp.views import principal, new_eixo, editar_eixo, deletar_eixo, index, login, register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('principal/', principal, name='principal'),
    path('new_eixo/', new_eixo, name='new_eixo'),
    path('editar_eixo/<str:id>', editar_eixo, name='editar_eixo'),
    path('deletar/<str:id>',deletar_eixo, name='deletar_eixo'),
    path('',index, name='index'),
    path('login',login, name='login'),
    path('register',register, name='register'),
]
