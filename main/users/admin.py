from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import MyUser, Profile


class InlineProfile(admin.StackedInline):
    model = Profile
    verbose_name = 'Profile'
    verbose_name_plural = 'Profiles'
    can_delete = False


@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    inlines = (InlineProfile, )


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'bio')
