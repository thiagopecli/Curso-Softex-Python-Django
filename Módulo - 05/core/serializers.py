from rest_framework import serializers
from .models import Tarefa

class TarefaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tarefa
        fields = ['id', 'user', 'titulo', 'descricao', 'concluida', 'criada_em']
        read_only_fields = ['id', 'criada_em']