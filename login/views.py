from django.shortcuts import render
from .models import Conta
from .forms import CriarConta


# Create your views here.

class ContaAcoes():

    def conta_cadastro(request):
        if request.method == 'POST':

            django_form = CriarConta(request.POST)
            if django_form.is_valid():
                """ Assign data in Django Form to local variables """
                novo_membro_email = django_form.data.get('email')
                novo_membro_senha = django_form.data.get("senha")
                
                """ This is how your model connects to database and create a new member """
                Conta.objects.create(
                    email = novo_membro_email, 
                    senha = novo_membro_senha
                    )
                
                return render(request, 'login/login.html')
            
            else:
                """ redirect to the same page if django_form goes wrong """
                return render(request, 'login/cadastro.html')

        else:
            return render(request, 'login/cadastro.html')
        
    def conta_deletar(request, pk):
        try:
            Conta.objects.filter(id = pk).delete()   
            return render(request, 'login/login.html')

        except Conta.DoesNotExist:
            return render(request, 'heroes/myprofile.html')

    def login(request, codinome, senha):
        if request.method == 'POST':
            from django.contrib.auth import authenticate, login

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return render(request, 'heroes/myprofile.html')
            else:
                return render(request, 'login/login.html')

        else:
            return render(request, 'login/login.html',  {'error': 'Credenciais inválidas'})


    def logout(request):
        pass

