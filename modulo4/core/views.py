from django.shortcuts import render
from django.http import HttpResponse
from .models import Tarefa
from .models import Execucao

# Create your views here.
def home(request):
    # return HttpResponse("<h1>Olá, Mundo! Esta é minha primeira página Django!</h1>")
    todas_as_tarefas = Tarefa.objects.all()
    todas_as_execucoes = Execucao.objects.all()
    context = {
        'nome_usuario': 'Thiago',
        'tecnologias':['Python','Django','HTML','CSS'],
        'tarefas': todas_as_tarefas,
        'execucoes': todas_as_execucoes,
    }
    return render(request, 'home.html', context)

def sobre(request):
    return HttpResponse("<h1>Sobre:</h1>"
    "<h2> Django é uma framework de alto nível.</h2>")