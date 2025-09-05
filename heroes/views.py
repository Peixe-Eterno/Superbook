from django.shortcuts import render, redirect
from .models import Hero
from .forms import ContatoForm, HeroForm

# Create your views here.
def show_heroes(request):
    return render(request, 'heroes/lista_herois.html', {'herois': Hero.objects.all()})

def contato_view(request):
    form = ContatoForm()  # formulário vazio

    if request.method == "POST":
        form = ContatoForm(request.POST)
        if form.is_valid():
            # Aqui você poderia enviar um e-mail ou salvar no banco
            print(form.cleaned_data)
            return render(request, "heroes/contato_sucesso.html")

    return render(request, "heroes/contato.html", {"form": form})

def criar_heroi(request):
    if request.method == "POST":
        form = HeroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_herois')
    else:
        form = HeroForm()

    return render(request, "heroes/form_heroi.html", {"form": form})
