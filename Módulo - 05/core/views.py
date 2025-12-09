from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from django.db.models import Count, Q

from .models import Tarefa
from .serializers import TarefaSerializer

class ListaTarefasAPIView(APIView):
    def get(self, request, format=None):
        user_id = request.query_params.get('user_id')

        if user_id:
            tarefas = Tarefa.objects.filter(user_id=user_id)
        else:
            tarefas = Tarefa.objects.all()
        
        serializer = TarefaSerializer(
            tarefas,
            many=True,
            context={'request': request},
        )
        return Response(serializer.data)

    def post(self, request, format=None):
        try:
            serializer = TarefaSerializer(
                data=request.data,
                context={'request': request},
            )

            if serializer.is_valid():
                serializer.save()
                return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED
                )

            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        except IntegrityError as e:
            # Erro de constraint no banco (ex: UNIQUE)
            return Response(
                {'error': 'Violação de integridade no banco de dados.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        except Exception as e:
            # Erro inesperado
            return Response(
                {'error': 'Erro interno do servidor.'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class ContagemTarefasAPIView(APIView):
    def get(self, request):
        agregados = Tarefa.objects.aggregate(
            total=Count('id'),
            concluidas=Count('id', filter=Q(concluida=True)),
        )
        total = agregados['total']
        concluidas = agregados['concluidas']
        pendentes = total - concluidas

        return Response({
            'total': total,
            'concluidas': concluidas,
            'pendentes': pendentes,
        })

class EstatisticasTarefasAPIView(APIView):
    def get(self, request):
        agregados = Tarefa.objects.aggregate(
            total=Count('id'),
            concluidas=Count('id', filter=Q(concluida=True)),
        )

        total = agregados['total']
        concluidas = agregados['concluidas']
        pendentes = total - concluidas
        taxa_conclusao = concluidas / total if total > 0 else 0

        return Response({
            'total': total,
            'concluidas': concluidas,
            'pendentes': pendentes,
            'taxa_conclusao': round(taxa_conclusao, 2),
        })