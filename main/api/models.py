from django.db import models


class GPA(models.Model):
    subjects_num = models.IntegerField(default=0)


class Subject(models.Model):
    subject_id = models.CharField()
    name = models.CharField(max_length=100)
    prerequisite = models.ForeignKey('self')

    def __str__(self):
        return self.name


class Student(models.Model):
    student_id = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    # gpa = models.FloatField()


class Teacher(models.Model):
    pass


class OfReg(models.Model):
    pass


class Schedule(models.Model):
    pass

