from rest_framework import serializers

from .models import Subject, TeacherSubject, SubjectStudent, TakenSubject, AttendanceStudent, News
from .constants import TEACHER, STUDENT
from users.serializers import MyUserSerializer


class SubjectSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    course_code = serializers.CharField()
    semester = serializers.CharField()

    def create(self, validated_data):
        subject = Subject(**validated_data)
        subject.save()
        return subject

    def update(self, instance, validated_data):
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


class TeacherSubjectSerializer(serializers.ModelSerializer):
    teacher = MyUserSerializer(read_only=True)
    teacher_id = serializers.IntegerField(write_only=True)
    subject = SubjectSerializer(read_only=True)
    subject_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = TeacherSubject
        fields = ('teacher', 'subject', 'teacher_id', 'subject_id', 'course_code', 'semester')

    def validate_teacher(self, teacher):
        if teacher.role != TEACHER:
            raise serializers.ValidationError('Teacher must be provided for creating Teacher Subject')
        return teacher


class SubjectStudentSerializer(serializers.ModelSerializer):
    student = MyUserSerializer(read_only=True)
    student_id = serializers.IntegerField(write_only=True)
    subject = SubjectSerializer(read_only=True)
    subject_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = SubjectStudent
        fields = ('student', 'student_id', 'subject', 'subject_id')

    def validate_student(self, student):
        if student.role != STUDENT:
            raise serializers.ValidationError('Student must be provided for creating Subject Student')
        return student


class TakenSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = TakenSubject
        fields = '__all__'

    def create(self, validated_data):
        taken_subject = TakenSubject(**validated_data)
        taken_subject.save()
        return taken_subject

    def update(self, instance, validated_data):
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance

    def validate_teacher(self, teacher):
        if teacher.role != TEACHER:
            raise serializers.ValidationError('Teacher must be provided for creating Teacher Subject Marks for Student')
        return teacher


class StudentTakenSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = TakenSubject
        fields = '__all__'

    def validate_student(self, student):
        if student.role != STUDENT:
            raise serializers.ValidationError('Student must be provided for view Subject Student Marks')
        return student


class TeacherAttendanceStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceStudent
        fields = '__all__'

    def create(self, validated_data):
        attendance_for = AttendanceStudent(**validated_data)
        attendance_for.save()
        return attendance_for

    def update(self, instance, validated_data):
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance

    def validate_teacher(self, teacher):
        if teacher.role != TEACHER:
            raise serializers.ValidationError('Teacher must be provided for creating Teacher Subject Marks for Student')
        return teacher


class AttendanceStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceStudent
        fields = '__all__'

    def validate_student(self, student):
        if student.role != STUDENT:
            raise serializers.ValidationError('Student must be provided for view Subject Student Marks')
        return student


class NewsSerializer(serializers.Serializer):
    class Meta:
        model = News

        fields = ('title',)
