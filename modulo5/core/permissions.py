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
