from django.db import models
from django.contrib.auth.models import User

class Tarefa(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=200) # equivale a text no sql
    concluida = models.BooleanField(default=False) # equivale a bool
    criada_em = models.DateTimeField(auto_now_add=True) # coloca a data em que os dados foram criados

    def __str__(self):
        return self.titulo

class Execucao(models.Model):
    nome = models.CharField(max_length=200)
    local = models.CharField(max_length=200)
    hora = models.DateTimeField(auto_now_add=True)
    concluido = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
