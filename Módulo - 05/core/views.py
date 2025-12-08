from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Tarefa
from .serializers import TarefaSerializer

class ListaTarefasAPIView(APIView):
    """
    View para listar todas as tarefas (GET).
    Endpoints:
    GET /api/tarefas/ - Lista todas as tarefas
    """
    def get(self, request, format=None):
        user_id = request.query_params.get('user_id')

        if user_id:
            tarefas = Tarefa.objects.filter(user_id=user_id)
        else:
            tarefas = Tarefa.objects.all()
        
        serializer = TarefaSerializer(tarefas, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TarefaSerializer(data=request.data)

    # 2. VALIDAR: Checar se os dados são válidos
        if serializer.is_valid():
    # 3. SALVAR: Persistir no banco de dados
            serializer.save()

    # 4. RESPONDER: Retornar objeto criado + status 201
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
                )

    # 5. ERRO: Retornar erros de validação + status 400
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class ContagemTarefasAPIView(APIView):
    def get(self, request):
        total = Tarefa.objects.count()
        concluidas = Tarefa.objects.filter(concluida=True).count()
        pendentes = total - concluidas

        return Response({'total': total, 'concluidas': concluidas, 'pendentes': pendentes
})
