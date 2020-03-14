from django.db import models
from django.contrib.auth.models import AbstractUser

from .constants import USER_ROLES_CHOICES, STUDENT


class MyUser(AbstractUser):
    role = models.PositiveSmallIntegerField(choices=USER_ROLES_CHOICES, default=STUDENT)


class Profile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)

