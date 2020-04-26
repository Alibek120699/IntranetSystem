from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import MyUser, Profile, ProfileTeacher, ProfileStudent


class InlineProfile(admin.StackedInline):
    model = Profile
    verbose_name = 'Profile'
    verbose_name_plural = 'Profiles'
    can_delete = False


@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    inlines = (InlineProfile,)


@admin.register(ProfileTeacher)
class ProfileTeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'bio', 'img', 'position')


@admin.register(ProfileStudent)
class ProfileStudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'bio', 'img', 'faculty')
