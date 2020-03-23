from rest_framework import serializers

from .models import Subject, TeacherSubject, SubjectStudent
from main.constants import TEACHER, STUDENT


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
