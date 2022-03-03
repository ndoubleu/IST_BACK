from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user or request.user.is_superuser

class IsSuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser
    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser
