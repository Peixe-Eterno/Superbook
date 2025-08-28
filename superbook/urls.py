"""
URL configuration for superbook project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from heroes import views
from login import views
from contato import views
from posts import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # login urls
    path('superbook/login/', views.login, name='login'),
    path('superbook/login/', views.logout, name='logout'),
    path('superbook/cadastro/', views.cadastro, name='cadastro'),

    # posts urls
    path('superbook/posts/', views.show_posts, name='show_posts'),
    path('superbook/posts/', views.dar_like, name='like'),
    path('superbook/posts/', views.dar_deslike, name='deslike'),
    path('superbook/posts/', views.comentar, name='comentar'),
    path('superbook/posts/', views.deletar_comentario, name='deletar_comentario'),

    # heroes(Profile) urls
    path('superbook/heroes/<int:pk>', views.show_heroes, name='show_heroes'),
    path('superbook/myprofile/', views.show_hero, name='show_hero'),

    # contato(Messages) urls
    path('superbook/contato/', views.show_contato, name='show_contato'),
    path('superbook/contato/<int:pk>/', views.conversa, name='conversa'),
]
