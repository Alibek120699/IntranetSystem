from rest_framework.permissions import BasePermission

from .constants import TEACHER, OFFICE_REGISTER, STUDENT


class IsAllowedToMark(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == TEACHER


class IsAllowedToViewSubjectStudents(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == TEACHER


class IsAllowedToViewTakenSubjectMarkStudents(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == STUDENT


class IsAllowedToViewAttendance(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == STUDENT


class IsAllowedToCheckAttendance(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == TEACHER


# class IsAllowedToCheckAttendance(BaseException):
#     def has_permission(self, request, view):
#         return request.user.role == TEACHER


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
