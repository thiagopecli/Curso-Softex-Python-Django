from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Tarefa
from .serializers import TarefaSerializer
from django.db import IntegrityError
import logging
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import UserRegistrationSerializer
from django.contrib.auth.models import User
from .permissions import IsGerente

logger = logging.getLogger(__name__)

class ListaTarefasAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user_id = request.query_params.get('user_id')
        if user_id:
            tarefas = Tarefa.objects.filter(user_id=user_id)
        else:
            tarefas = Tarefa.objects.all()
            
        serializer = TarefaSerializer(tarefas, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        try:
            serializer = TarefaSerializer(data=request.data)
            if serializer.is_valid():
                tarefa_criada = serializer.save(user=self.request.user)
                logger.info(f"Tarefa criada: {tarefa_criada.id}")
                return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED
                )
            logger.warning(f"Validação falhou: {serializer.errors}")
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        except IntegrityError as e:
            return Response(
                {'error': 'Violação de integridade no banco de dados.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            logger.error(f"Erro ao criar tarefa: {str(e)}")
            return Response(
                {'error': 'Erro interno do servidor.'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class DetalheTarefaAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get_object(self, pk):
        return get_object_or_404(Tarefa, pk=pk)
    
    def get(self, request, pk, format=None):
        tarefa = self.get_object(pk)
        serializer = TarefaSerializer(tarefa)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk, format=None):
        tarefa = self.get_object(pk)
        serializer = TarefaSerializer(tarefa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk, format=None):
        tarefa = self.get_object(pk)
        serializer = TarefaSerializer(tarefa, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        tarefa = self.get_object(pk)
        tarefa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def post(self, request, pk, formt=None):
        tarefa_original = self.get_object(pk)
        data = dict(TarefaSerializer(tarefa_original).data)
        data.pop("id", None)
        data["concluida"] = False

        serializer = TarefaSerializer(data=data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
class ContagemTarefasAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        total = Tarefa.objects.count()
        concluidas = Tarefa.objects.filter(concluida=True).count()
        pendentes = total - concluidas
        return Response({
        'total': total,
        'concluidas': concluidas,
        'pendentes': pendentes
})

class EstatisticasTarefasAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        total = Tarefa.objects.count()
        concluidas = Tarefa.objects.filter(concluida=True).count()
        pendentes = Tarefa.objects.filter(concluida=False).count()
        
        taxa_conclusao = concluidas / total if total > 0 else 0
        
        return Response({
        'total': total,
        'concluidas': concluidas,
        'pendentes': pendentes,
        'taxa_conclusao': round(taxa_conclusao, 2)
        })
    
class ConcluirTarefaLoteAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def patch(self, request, format=None):
        ids = request.data.get("ids", [])

        if not isinstance(ids, list) or len(ids) == 0:
            return Response({"error": "Envie uma lista de IDs"}, status=status.HTTP_400_BAD_REQUEST)
        
        atualizadas = Tarefa.objects.filter(id__in=ids).update(concluida=True)

        return Response(
            {
                "mensagem": "Tarefas atualizadas com sucesso!",
                "quantidade": atualizadas,
                "ids": ids
            },
            status=status.HTTP_200_OK
        )

class MinhaView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response(f"Usuario autenticado: {request.user.username}",
                        status=status.HTTP_200_OK)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(
                {"detail": "Logout realizado com sucesso."},
                status=status.HTTP_205_RESET_CONTENT
                )
        except Exception:
            return Response(
                {"detail": "Token inválido."},
                status=status.HTTP_400_BAD_REQUEST
            )

class MeView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = request.user
        return Response({
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'is_staff': user.is_staff,
            'date_joined': user.date_joined
        })

class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        user = request.user
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')
        
        if not user.check_password(old_password):
            return Response(
                {'error': 'Senha atual incorreta'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        user.set_password(new_password)
        user.save()
        return Response({'detail': 'Senha alterada com sucesso'})

class StatsView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = request.user
        tarefas_usuario = Tarefa.objects.filter(user=user)
        
        total_tarefas = tarefas_usuario.count()
        concluidas = tarefas_usuario.filter(concluida=True).count()
        pendentes = tarefas_usuario.filter(concluida=False).count()
        
        taxa_conclusao = concluidas / total_tarefas if total_tarefas > 0 else 0
        
        return Response({
            'total_tarefas': total_tarefas,
            'concluidas': concluidas,
            'pendentes': pendentes,
            'taxa_conclusao': round(taxa_conclusao, 2)
        })

class TarefaListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = TarefaSerializer
    permission_classes = [IsAuthenticated] # Exige Token válido
    
    def get_queryset(self):
        """
        Sobrescreve o comportamento padrão para retornar APENAS
        os dados pertencentes ao usuário logado.
        """
        user = self.request.user
        return Tarefa.objects.filter(user=user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TarefaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TarefaSerializer    
    def get_queryset(self):
        """
        Garante que operações de detalhe (GET, PUT, DELETE por ID)
        só encontrem o objeto se ele pertencer ao usuário.
        Gerentes ou superusers podem acessar todas as tarefas.
        """
        user = self.request.user

        if user.is_superuser or user.groups.filter(name='Gerente').exists():
            return Tarefa.objects.all()
        return Tarefa.objects.filter(user=user)
    def get_permissions(self):
        """
        Instancia e retorna a lista de permissões que esta view requer,
        dependendo do método HTTP da requisição.
        """
        if self.request.method == 'DELETE':
            return [IsAuthenticated(), IsGerente()]
        return [IsAuthenticated()]


class RegisterView(generics.CreateAPIView):
    """
    Endpoint para cadastro de novos usuários.
    Acesso: Público (Qualquer um pode criar conta).
    """
    queryset = User.objects.all()
    permission_classes = [AllowAny] # Sobrescreve o padrão global
    serializer_class = UserRegistrationSerializer
