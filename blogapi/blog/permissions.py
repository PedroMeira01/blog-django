from rest_framework import permissions

class IsUserCreateOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method == 'POST'
