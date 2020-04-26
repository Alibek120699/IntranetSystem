from django.db import models

A = "A"
B = "B"
C = "C"
D = "D"
F = "F"
GRADE = (
    (A, 'A'),
    (B, 'B'),
    (C, 'C'),
    (D, 'D'),
    (F, 'F'),
)

PASS = "PASS"
FAIL = "FAIL"
STATUS = (
    (PASS, "PASS"),
    (FAIL, "FAIL"),
)
FIRST = "First"
SECOND = "Second"
SEMESTER = (
    (FIRST, "First"),
    (SECOND, "Second"),
)
PARTICIPATE = "P"
NOTPARTICIPATE = "NP"
ATTENDANCE = (
    (PARTICIPATE, "PARTICIPATE"),
    (NOTPARTICIPATE, "NOTPARTICIPATE"),
)


class Subject(models.Model):
    name = models.CharField(max_length=20)
    course_code = models.CharField(max_length=200, default="CS1102")
    description = models.TextField(max_length=500, null=True, blank=True)
    semester = models.CharField(choices=SEMESTER, max_length=20, default=FIRST)

    def __str__(self):
        return f'{self.name}: {self.course_code}: {self.description}'


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


class TakenSubject(models.Model):
    subject = models.ForeignKey(Subject,
                                on_delete=models.CASCADE, )
    student = models.ForeignKey('users.MyUser',
                                on_delete=models.CASCADE)
    first_att = models.PositiveIntegerField(blank=True, null=True, default=0)
    second_att = models.PositiveIntegerField(blank=True, null=True, default=0)
    final = models.PositiveIntegerField(blank=True, null=True, default=0)
    total = models.PositiveIntegerField(blank=True, null=True, default=0)
    grade = models.CharField(choices=GRADE, max_length=1, blank=True)
    status = models.CharField(choices=STATUS, max_length=200, blank=True)

    def get_total(self, first_att, second_att, final):
        return int(first_att) + int(second_att) + int(final)

    def get_grade(self, first_att, second_att, final):
        total = int(first_att) + int(second_att) + int(final)
        if total >= 70:
            grade = A
        elif total >= 60:
            grade = B
        elif total >= 50:
            grade = C
        elif total >= 45:
            grade = D
        else:
            grade = F
        return grade

    def get_status(self, grade):
        if not grade == "F":
            comment = PASS
        else:
            comment = FAIL
        return comment


class AttendanceStudent(models.Model):
    subject = models.ForeignKey(Subject,
                                on_delete=models.CASCADE, )
    student = models.ForeignKey('users.MyUser',
                                on_delete=models.CASCADE)
    attendance = models.CharField(choices=ATTENDANCE, max_length=50, default=PARTICIPATE)
