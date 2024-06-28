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
from django.template.defaulttags import url
from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.views.static import serve
from django.conf import settings
from cpasisApp.views import principal, new_eixo, editar_eixo, deletar_eixo, editar_dim,deletar_dim, new_dim
from cpasisApp.views import new_ind, editar_ind, deletar_ind, new_campus, editar_campus, deletar_campus, avaliar_ind
from cpasisApp.views import new_pub, deletar_publico, editar_publico, new_tipo, editar_tipo, deletar_tipo,editar_curso,new_curso,deletar_curso,home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('principal', principal, name='principal'),
    path('home/', home, name='home'),
    path('new_eixo/', new_eixo, name='new_eixo'),
    path('editar_eixo/<str:id>', editar_eixo, name='editar_eixo'),
    path('deletar/<str:id>',deletar_eixo, name='deletar_eixo'),
    # dimensão
    path('new_dim/', new_dim, name='new_dim'),
    path('editar_dim/<str:id>', editar_dim, name='editar_dim'),
    path('deletar_dim/<str:id>',deletar_dim, name='deletar_dim'),
    #indicadores
    path('new_ind/', new_ind, name='new_ind'),
    path('editar_ind/<str:id>', editar_ind, name='editar_ind'),
    path('deletar_ind/<str:id>',deletar_ind, name='deletar_ind'),
    # campus
    path('new_campus/', new_campus, name='new_campus'),
    path('editar_campus/<str:id>', editar_campus, name='editar_campus'),
    path('deletar_campus/<str:id>',deletar_campus, name='deletar_campus'),
    #publico
    path('new_publico/', new_pub, name='new_pub'),
    path('editar_publico/<str:id>', editar_publico, name='editar_publico'),
    path('deletar_publico/<str:id>', deletar_publico, name='deletar_publico'),
    #tipo
    path('new_tipo/', new_tipo, name='new_tipo'),
    path('editar_tipo/<str:id>', editar_tipo, name='editar_tipo'),
    path('deletar_tipo/<str:id>', deletar_tipo, name='deletar_tipo'),
    #curso
    path('new_curso/', new_curso, name='new_curso'),
    path('editar_curso/<str:id>', editar_curso, name='editar_curso'),
    path('deletar_curso/<str:id>', deletar_curso, name='deletar_curso'),

    #usuários
    path('', include('usuariosApp.urls')),

    #avaliar
    path('avaliar_ind',avaliar_ind ,name='avaliar_ind'),

    re_path(r'^img/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),




]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
