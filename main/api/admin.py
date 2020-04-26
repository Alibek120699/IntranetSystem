from django.contrib import admin

from .models import Subject, TeacherSubject, SubjectStudent, TakenSubject, AttendanceStudent


# TakenSubjectStudent


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')


@admin.register(TeacherSubject)
class TeacherSubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'teacher', 'subject')


@admin.register(SubjectStudent)
class SubjectStudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'student')


@admin.register(TakenSubject)
class TakenSubject(admin.ModelAdmin):
    list_display = ('id', 'subject', 'student')


@admin.register(AttendanceStudent)
class AttendanceStudent(admin.ModelAdmin):
    list_display = ('id', 'subject', 'student', 'attendance')
