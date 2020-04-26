from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

from .validators import validate_extension, validate_file_size
from .constants import USER_ROLES_CHOICES, STUDENT, TEACHER, OFFICE_REGISTER

LECTOR = "LECTOR"
TUTOR = "TUTOR"
PROFESSOR = "PROFESSOR"
ASSISTANT = "ASSISTANT"

POSITION = (
    (LECTOR, "LECTOR"),
    (TUTOR, "TUTOR"),
    (PROFESSOR, "PROFESSOR"),
    (ASSISTANT, "ASSISTANT")
)

FIT = "FIT"
BIS = "BIS"
ISE = "ISE"
MKA = "MKA"

FACULTY = (
    (FIT, "FIT"),
    (BIS, "BIS"),
    (ISE, "ISE"),
    (MKA, "MKA"),

)


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
    img = models.ImageField(upload_to='profile_photos',
                            validators=[validate_file_size,
                                        validate_extension],
                            null=True, blank=True)

    def __str__(self):
        return f'{self.user}: {self.bio}'

    class Meta:
        abstract = True

class ProfileTeacher(Profile):
    position = models.CharField(choices=POSITION, max_length=50, blank=True)


class ProfileStudent(Profile):
    faculty = models.CharField(choices=FACULTY, max_length=50, blank=True)
