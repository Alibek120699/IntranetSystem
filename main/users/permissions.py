from rest_framework.permissions import BasePermission

from .constants import TEACHER, OFFICE_REGISTER, STUDENT


class IsAllowedToCreateTeacherProfile(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == TEACHER


class IsAllowedToCreateStudentProfile(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == STUDENT
