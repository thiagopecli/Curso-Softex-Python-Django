from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("<h1>Olá, Mundo! Esta é minha primeira página Django!</h1>")
    context = {
        'nome_usuario': 'Thiago',
        'tecnologias':['Python','Django','HTML','CSS']
    }
    return render(request, 'home.html', context)

def sobre(request):
    return HttpResponse("<h1>Sobre:</h1>"
    "<h2> Django é uma framework de alto nível.</h2>")