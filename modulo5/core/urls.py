from django.urls import path
from .views import (
    ListaTarefasAPIView,
    ContagemTarefasAPIView,
    EstatisticasTarefasAPIView,
    DetalheTarefaAPIView,
    ConcluirTarefaLoteAPIView,
    MinhaView,
    LogoutView,
    MeView,
    ChangePasswordView,
    StatsView,
    TarefaListCreateAPIView,
    TarefaRetrieveUpdateDestroyAPIView,
    RegisterView
)

app_name = 'core'
urlpatterns = [
    path('tarefas/', TarefaListCreateAPIView.as_view(), name='tarefas-list'),
    path('tarefas/<int:pk>/', TarefaRetrieveUpdateDestroyAPIView.as_view(), name='tarefas-detail'),
    path('tarefas/contagem/', ContagemTarefasAPIView.as_view(), name='contagem-tarefas'),
    path('tarefas/estatisticas/', EstatisticasTarefasAPIView.as_view(), name='estatisticas-tarefas'),
    path('tarefas/<int:pk>/duplicar/', DetalheTarefaAPIView.as_view()),
    path('tarefas/concluir-todas/', ConcluirTarefaLoteAPIView.as_view()),
    path('teste/', MinhaView.as_view(), name='teste-autenticidade'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('me/', MeView.as_view(), name='me'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('stats/', StatsView.as_view(), name='stats'),
    path('register/', RegisterView.as_view(), name='register'),
]