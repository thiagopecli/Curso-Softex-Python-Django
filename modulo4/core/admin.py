from django.contrib import admin
from .models import Tarefa
from .models import Execucao

admin.site.register(Tarefa)
admin.site.register(Execucao)