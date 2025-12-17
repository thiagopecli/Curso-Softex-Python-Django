from django.urls import path
from .views import ListaTarefasAPIView
from .views import ContagemTarefasAPIView
from .views import EstatisticasTarefasAPIView
from .views import DetalheTarefaAPIView
from .views import ConcluirTarefaLoteAPIView
from .views import MinhaView
from .views import LogoutView
from .views import MeView, ChangePasswordView, StatsView

app_name = 'core'
urlpatterns = [
    path('tarefas/', ListaTarefasAPIView.as_view(), name='lista-tarefas'),
    path('tarefas/user_id=1', ListaTarefasAPIView.as_view(), name='lista-tarefas'),
    path('tarefas/contagem/', ContagemTarefasAPIView.as_view(), name='contagem-tarefas'),
    path('tarefas/estatisticas/', EstatisticasTarefasAPIView.as_view(), name='estatisticas-tarefas'),
    path('tarefas/<int:pk>/', DetalheTarefaAPIView.as_view(), name='detalhe-tarefa'),
    path('tarefas/<int:pk>/duplicar/', DetalheTarefaAPIView.as_view()),
    path('tarefas/concluir-todas/', ConcluirTarefaLoteAPIView.as_view()),
    path('teste/', MinhaView.as_view(), name= 'teste-autenticidade'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('me/', MeView.as_view(), name='me'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('stats/', StatsView.as_view(), name='stats'),
]