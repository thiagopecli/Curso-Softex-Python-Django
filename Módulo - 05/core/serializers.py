from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework import serializers

from .models import Tarefa


class TarefaSerializer(serializers.ModelSerializer):
    titulo = serializers.CharField(
        max_length=200,
        error_messages={
            'required': 'O título é obrigatório.',
            'blank': 'O título não pode ser vazio.',
            'max_length': 'O título não pode ter mais de 200 caracteres.',
        },
    )
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        required=False,
        default=serializers.CurrentUserDefault(),
    )
    prioridade = serializers.ChoiceField(
        choices=Tarefa.PRIORIDADE_CHOICES,
        default='media',
    )
    prazo = serializers.DateField(required=False, allow_null=True)

    class Meta:
        model = Tarefa
        fields = [
            'id',
            'user',
            'titulo',
            'descricao',
            'prioridade',
            'prazo',
            'concluida',
            'criada_em',
        ]
        read_only_fields = ['id', 'criada_em']

    def validate_titulo(self, value):
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

        request = self.context.get('request')
        request_user = getattr(request, 'user', None)
        initial_data = getattr(self, 'initial_data', {})
        raw_user = initial_data.get('user') if isinstance(initial_data, dict) else None

        user = None
        if isinstance(raw_user, User):
            user = raw_user
        elif raw_user is not None:
            try:
                user = User.objects.get(pk=raw_user)
            except User.DoesNotExist:
                user = None

        if user is None and request_user and request_user.is_authenticated:
            user = request_user

        if user and Tarefa.objects.filter(user=user, titulo=value).exists():
            raise serializers.ValidationError(
                "Você já tem uma tarefa com este título."
            )

        return value

    def validate_prioridade(self, value):
        escolhas_validas = {choice[0] for choice in Tarefa.PRIORIDADE_CHOICES}
        if value not in escolhas_validas:
            raise serializers.ValidationError("Prioridade inválida.")
        return value

    def validate(self, attrs):
        user_from_attrs = attrs.get('user')
        request_user = getattr(self.context.get('request'), 'user', None)

        if user_from_attrs is None and request_user and request_user.is_authenticated:
            attrs['user'] = request_user
        elif user_from_attrs is None:
            raise serializers.ValidationError(
                {"user": "Usuário é obrigatório."}
            )

        prazo_atual = self.instance.prazo if self.instance else None
        concluida_atual = self.instance.concluida if self.instance else False

        prazo = attrs.get('prazo', prazo_atual)
        concluida = attrs.get('concluida', concluida_atual)

        if prazo:
            today = timezone.localdate()
            if prazo < today:
                raise serializers.ValidationError(
                    {"prazo": "O prazo não pode ser no passado."}
                )

        if concluida is False and prazo is None:
            raise serializers.ValidationError(
                {"prazo": "Prazo é obrigatório para tarefas pendentes."}
            )

        return attrs