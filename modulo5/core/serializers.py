from rest_framework import serializers
from .models import Tarefa
from datetime import date
from django.utils import timezone

class TarefaSerializer(serializers.ModelSerializer):
    titulo = serializers.CharField(
        max_length=200,
        error_messages={
            'required': 'O título é obrigatório.',
            'blank': 'O título não pode ser vazio.',
            'max_length': 'O título não pode ter mais de 200 caracteres.'
            }
        )
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Tarefa
        fields = ['id', 'user', 'titulo', 'prioridade', 'descricao', 'prazo', 'concluida', 'data_conclusao' ,'criada_em']
        read_only_fields = ['id', 'user', 'criada_em']
    def validate(self, data):
        '''Implemente validação customizada:
        • O prazo não pode ser no passado
        • Se concluida=True, prazo não é obrigatório
        • Se concluida=False, prazo é obrigatório '''
        prazo = data.get('prazo')
        concluida = data.get('concluida', False)
        if prazo and prazo < date.today():
            raise serializers.ValidationError(
                "O prazo não pode ter data retroativa."
            )
        if concluida is False and prazo is None:
            raise serializers.ValidationError(
                "Tarefa não conluída o prazo é obrigatório!"
            )
        return data
    
    def validate_titulo(self, value):
        """
        Validação customizada para o campo 'titulo'.
        Regras:
        - Não pode ser vazio (após strip)
        - Não pode conter apenas números
        - Deve ter pelo menos 3 caracteres
        """
        value = value.strip()
        if not value:
            raise serializers.ValidationError(
                "O título não pode ser vazio ou conter apenas espaços."
            )
        if len(value) < 3:
            raise serializers.ValidationError(
                "O título deve ter pelo menos 3 caracteres."
            )
        if value.isdigit():
            raise serializers.ValidationError(
                "O título não pode conter apenas números."
            )
            
        return value
    
    def update(self, instance, validated_data):
        concluida_atual = instance.concluida
        concluida_nova = validated_data.get("concluida", concluida_atual)

        if not concluida_atual and concluida_nova is True:
            instance.data_conclusao = timezone.now()

        if concluida_atual and concluida_nova is False:
            instance.data_conclusao = None

        return super().update(instance, validated_data)