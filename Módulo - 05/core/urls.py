from django.urls import path
from .views import ListaTarefasAPIView
from .views import ContagemTarefasAPIView

app_name = 'core'
urlpatterns = [
        path('tarefas/', ListaTarefasAPIView.as_view(), name='lista-tarefas'),
        path('tarefas/user_id=1', ListaTarefasAPIView.as_view(), name='lista-tarefas'),
        path('tarefas/contagem/', ContagemTarefasAPIView.as_view(), name='contagem-tarefas'),
]
