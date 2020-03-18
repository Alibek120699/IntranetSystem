from django.contrib import admin

from .models import Subject, TeacherSubject, SubjectStudent


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')


@admin.register(TeacherSubject)
class TeacherSubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'teacher', 'subject')


@admin.register(SubjectStudent)
class SubjectStudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'student')
