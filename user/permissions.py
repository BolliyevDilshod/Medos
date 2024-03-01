from rest_framework import permissions
from .exceptions import BaseAPIException

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_admin()

class IsDoctor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_doctor()

class IsHospital(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_hospital()