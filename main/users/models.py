from django.db import models
from django.contrib.auth.models import AbstractUser

from .constants import USER_ROLES_CHOICES, STUDENT, TEACHER, OFFICE_REGISTER


class MyUserManager(models.Manager):
    def get_teachers(self):
        return self.filter(role=TEACHER)

    def get_students(self):
        return self.filter(role=STUDENT)

    def get_office_registers(self):
        return self.filter(role=OFFICE_REGISTER)

    def get_users(self):
        return self.all()


class MyUser(AbstractUser):
    role = models.PositiveSmallIntegerField(choices=USER_ROLES_CHOICES, default=STUDENT)

    objects = MyUserManager()

    def __str__(self):
        return f'{self.username}: {self.role}'


class Profile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)

