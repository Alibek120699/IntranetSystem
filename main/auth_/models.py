from django.db import models
from django.contrib.auth.models import AbstractUser


class Role(models.Model):
    STUDENT = 1
    TEACHER = 2
    OFFICE_REGISTER = 3

    # is_teacher = models.BooleanField

    ROLE_CHOICES = (
        (STUDENT, 'STUDENT'),
        (TEACHER, 'TEACHER'),
        (OFFICE_REGISTER, 'OFFICE_REGISTER'),
    )

    id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)


class MyUser(AbstractUser):
    roles = models.ManyToManyField(Role)

    def change_password(self, new_password):
        self.password = new_password


class Profile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500)

    def __str__(self):
        return self.user.username
