from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f'{self.name}: {self.description}'


class TeacherSubject(models.Model):
    teacher = models.ForeignKey('users.MyUser',
                                on_delete=models.CASCADE,
                                related_name='subjects')
    # t = MyUser(role=TEACHER)
    # t.subjects.all()
    subject = models.ForeignKey(Subject,
                                on_delete=models.CASCADE,
                                related_name='teachers')
    # s = Subject()
    # s.teachers.all()

    def __str__(self):
        return f'{self.teacher} {self.subject}'


class SubjectStudent(models.Model):
    subject = models.ForeignKey(Subject,
                                on_delete=models.CASCADE,
                                related_name='students')
    # subj = Subject()
    # subj.students.all()
    student = models.ForeignKey('users.MyUser',
                                on_delete=models.CASCADE,
                                related_name='student_subjects')
    # stud = MyUser(role=STUDENT)
    # stud.student_subjects.all()

    def __str__(self):
        return f'{self.subject} {self.student}'

