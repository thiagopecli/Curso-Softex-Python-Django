from django.urls import path

from .views import ContagemTarefasAPIView, EstatisticasTarefasAPIView, ListaTarefasAPIView

app_name = 'core'
urlpatterns = [
        path('tarefas/', ListaTarefasAPIView.as_view(), name='lista-tarefas'),
        path('tarefas/user_id=1', ListaTarefasAPIView.as_view(), name='lista-tarefas'),
        path('tarefas/contagem/', ContagemTarefasAPIView.as_view(), name='contagem-tarefas'),
        path('tarefas/estatisticas/', EstatisticasTarefasAPIView.as_view(), name='estatisticas-tarefas'),
]
