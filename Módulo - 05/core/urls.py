from django.urls import path
from .views import ListaTarefasAPIView
from .views import ContagemTarefasAPIView
from .views import EstatisticasTarefasAPIView
from .views import DetalheTarefaAPIView
from .views import ConcluirTarefaLoteAPIView

app_name = 'core'
urlpatterns = [
    path('tarefas/', ListaTarefasAPIView.as_view(), name='lista-tarefas'),
    path('tarefas/user_id=1', ListaTarefasAPIView.as_view(), name='lista-tarefas'),
    path('tarefas/contagem/', ContagemTarefasAPIView.as_view(), name='contagem-tarefas'),
    path('tarefas/estatisticas/', EstatisticasTarefasAPIView.as_view(), name='estatisticas-tarefas'),
    path('tarefas/<int:pk>/', DetalheTarefaAPIView.as_view(), name='detalhe-tarefa'),
    path('tarefas/<int:pk>/duplicar/', DetalheTarefaAPIView.as_view()),
    path('tarefas/concluir-todas/', ConcluirTarefaLoteAPIView.as_view()),
]