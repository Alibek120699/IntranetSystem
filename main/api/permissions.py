from rest_framework.permissions import BasePermission

from main.constants import TEACHER, OFFICE_REGISTER


class IsAllowedToMark(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == TEACHER


class IsAllowedToViewScheduleOfStudents(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == TEACHER


class IsAllowedToCreateDiscipline(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == OFFICE_REGISTER


class IsAllowedToUpdateDiscipline(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == OFFICE_REGISTER


class IsAllowedToCreateTeacherSubject(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == OFFICE_REGISTER


class IsAllowedToCreateSubjectStudent(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == OFFICE_REGISTER
