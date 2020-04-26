from rest_framework import serializers

from .models import Subject, TeacherSubject, SubjectStudent, TakenSubject, AttendanceStudent
from .constants import TEACHER, STUDENT


class SubjectSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=True)

    def create(self, validated_data):
        subject = Subject(**validated_data)
        subject.save()
        return subject

    def update(self, instance, validated_data):
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


class TeacherSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherSubject
        fields = ('teacher', 'subject')

    def validate_teacher(self, teacher):
        if teacher.role != TEACHER:
            raise serializers.ValidationError('Teacher must be provided for creating Teacher Subject')
        return teacher


class SubjectStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectStudent
        fields = ('student', 'subject')

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
