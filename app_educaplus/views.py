from django.shortcuts import render, redirect
from .models import Estudante
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, get_user_model, logout
from django.contrib.auth.models import User

User = get_user_model() 


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        
        user = User.objects.get(email=email)
        user = authenticate(request, username=user.username, password=senha)
        if user is not None:
            auth_login(request, user)
            return redirect('painel')
        else:  
            messages.error(request, 'Erro. Revise os dados inseridos!')
    
    return render(request, 'usuarios/login.html')

    

def cadastro(request):
    return render(request, 'usuarios/registro.html')

def cadastrar(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha') 

        if nome and email and senha:

            novo_usuario = User.objects.create_user(username=nome, email=email, password=senha)
            novo_usuario.save()

            messages.success(request, 'Usuário cadastrado com sucesso!')
            return redirect('cadastro')

        else:
            messages.error(request, 'Por favor, preencha todos os campos.')

       
        return redirect('cadastro')
    
def sair(request):
    logout(request)
    return redirect('login')
def painel(request):
    usuario = request.user
    return render(request, 'usuarios/meu-painel.html', {'usuario': usuario})

    