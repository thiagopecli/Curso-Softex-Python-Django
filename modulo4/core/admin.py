from django.contrib import admin
from .models import Tarefa
from .models import Execucao

class TarefaAdmin(admin.ModelAdmin):
# 1. Adicione 'get_user_email' ao list_display
    list_display = ('titulo', 'user', 'get_user_email', 'concluida', 'criada_em')
    list_filter = ('concluida', 'user', 'criada_em')
    search_fields = ('titulo', 'user__username')
    fieldsets = (
    ('Informações Principais', {
    'fields': ('user', 'titulo')
    }),
    ('Status da Tarefa', {
    'fields': ('concluida', 'criada_em')
    }),
    )
    readonly_fields = ('criada_em',)
    # 2. Defina o método
    # O 'obj' é a instância da Tarefa que está sendo exibida na linha
    @admin.display(description='Email do Usuário') # Define o título da coluna
    def get_user_email(self, obj):
        return obj.user.email


admin.site.register(Tarefa, TarefaAdmin)
admin.site.register(Execucao)