from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

from .constants import USER_ROLES_CHOICES, STUDENT, TEACHER, OFFICE_REGISTER


class MyUserManager(UserManager):
    def get_teachers(self):
        return self.filter(role=TEACHER)

    def get_students(self):
        return self.filter(role=STUDENT)

    def get_office_registers(self):
        return self.filter(role=OFFICE_REGISTER)

    def create_user(self, username, person, password=None):
        if not username:
            raise ValueError('User must have a valid username')

        user = self.model(username=username, must_change_password=True, deleted=False,
                          person=person)

        user.set_password(password)
        user.save(using=self._db)
        return user


class MyUser(AbstractUser):
    role = models.PositiveSmallIntegerField(choices=USER_ROLES_CHOICES, default=STUDENT)

    objects = MyUserManager()

    def __str__(self):
        return f'{self.username}: {self.role}'


class Profile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)

