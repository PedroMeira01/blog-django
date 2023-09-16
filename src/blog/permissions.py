from rest_framework import permissions

class IsAuthenticatedOrUserCreateOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            # Permitir que qualquer usuário crie um novo usuário (POST)
            return True
        # Permitir leitura (GET), atualização (PUT) e exclusão (DELETE) apenas para usuários autenticados
        return request.user and request.user.is_authenticated

class IsAuthenticatedOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            # Permitir leitura (GET) para qualquer usuário (autenticado ou não)
            return True
        # Permitir criação, atualização e exclusão apenas para usuários autenticados
        return request.user and request.user.is_authenticated
