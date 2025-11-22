from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Tarefa
from .models import Execucao
from .forms import TarefaForm
# Create your views here.

@login_required
def home(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)

        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.user = request.user
            tarefa.save()
            return redirect('home')
    else:
        form = TarefaForm()
    # return HttpResponse("<h1>Olá, Mundo! Esta é minha primeira página Django!</h1>")
    todas_as_tarefas = Tarefa.objects.filter(user=request.user).order_by('-criada_em')
    todas_as_execucoes = Execucao.objects.all()
    context = {
        'nome_usuario': 'Thiago',
        'tecnologias': ['Python', 'Django', 'HTML', 'CSS'],
        'tarefas': todas_as_tarefas,
        'execucoes': todas_as_execucoes,
        'form': form,
    }
    return render(request, 'home.html', context)

def sobre(request):
    return HttpResponse("<h1>Sobre:</h1>"
                        "<h2> Django é uma framework de alto nível.</h2>")

@login_required
def concluir_tarefa(request, pk):
        # 1. Busca a tarefa pela 'pk' (ID) vinda da URL.
        # Se não achar, retorna um erro 404.
    tarefa = get_object_or_404(Tarefa, pk=pk, user=request.user)
    # 2. Segurança: Apenas execute se o método for POST
    if request.method == 'POST':
        # 3. A Lógica de "Update"
        tarefa.concluida = True
        tarefa.save()  # Não se esqueça de salvar!
        # 4. Redireciona de volta para a 'home' (Padrão PRG)
    return redirect('home')

@login_required
def deletar_tarefa(request, pk):
    # 1. Busca a tarefa
    tarefa = get_object_or_404(Tarefa, pk=pk, user=request.user)
        # 2. Segurança: Apenas execute se o método for POST
    if request.method == 'POST':
        # 3. A Lógica de "Delete"
        tarefa.delete()
        # 4. Redireciona de volta para a 'home'
    return redirect('home')

def register(request):
    # Se a requisição for POST, o usuário enviou o formulário
    if request.method == 'POST':
    # Cria uma instância do formulário com os dados enviados
        form = UserCreationForm(request.POST)
    # Verifica se o formulário é válido (ex: senhas batem, username não existe)
        if form.is_valid():
            user = form.save() # Salva o novo usuário no banco 
            login(request, user) # Faz o login automático do usuário
            return redirect('home') # Redireciona para a home
    # Se a requisição for GET, o usuário apenas visitou a página
    else:
        form = UserCreationForm() # Cria um formulário de cadastro vazio

    # Prepara o contexto e renderiza o template
    context = {'form': form}
    return render(request, 'register.html', context)