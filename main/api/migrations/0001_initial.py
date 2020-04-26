# Generated by Django 2.2.10 on 2020-04-25 20:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('courseCode', models.CharField(default='CS1102', max_length=200)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('semester', models.CharField(choices=[('FIRST', 'FIRST'), ('SECOND', 'SECOND')], default='FIRST', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TeacherSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teachers', to='api.Subject')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TakenSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_att', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('second_att', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('final_exam', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('total', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('grade', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F')], max_length=1)),
                ('status', models.CharField(blank=True, choices=[('PASS', 'PASS'), ('FAIL', 'FAIL')], max_length=50)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taken_subjects', to='api.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='SubjectStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_subjects', to=settings.AUTH_USER_MODEL)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='api.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='AttendanceStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance', models.CharField(blank=True, choices=[('P', 'P'), ('NP', 'NP')], max_length=50)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendance_student', to='api.Subject')),
            ],
        ),
    ]
