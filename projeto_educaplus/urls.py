from django.urls import path, include
from django.contrib.auth import views as auth_views
from app_educaplus import views


urlpatterns = [
    path("login/", views.login, name = 'login'),
    path('logout/', views.sair, name='logout'),
    path("cadastro/", views.cadastro, name = 'cadastro'),
    path("cadastrar/", views.cadastrar, name = 'cadastrar'),
    path("painel/", views.painel, name = 'painel'),
   
]
