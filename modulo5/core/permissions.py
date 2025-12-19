from rest_framework import permissions

class IsGerente(permissions.BasePermission):
    """
    Permissão customizada que concede acesso apenas se o usuário
    pertencer ao grupo 'Gerente'.
    """
    def has_permission(self, request, view) -> bool:
        if not request.user or not request.user.is_authenticated:
            return False
        return request.user.groups.filter(name='Gerente').exists()

class IsAdminOrOwner(permissions.BasePermission):
    """
    Permissão que concede acesso se:
    - O usuário é admin/staff (is_staff=True)
    - OU o usuário é o proprietário do objeto (é o criador)
    
    Isso permite que o suporte técnico (Admin) acesse qualquer tarefa para debug,
    enquanto usuários comuns só acessam suas próprias tarefas.
    """
    
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True        
        return obj.user == request.user
