from rest_framework import serializers

from .models import MyUser, Profile, ProfileTeacher, ProfileStudent


class MyUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = MyUser
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password', 'role')

    def create(self, validated_data):
        new_user = MyUser.objects.create_user(**validated_data)
        return new_user


class ProfileShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'user',)


class ProfileFullSerializer(ProfileShortSerializer):
    class Meta(ProfileShortSerializer.Meta):
        fields = ProfileShortSerializer.Meta.fields + ('bio',)


class ProfileTeacherSerializer(ProfileFullSerializer):
    class Meta(ProfileFullSerializer.Meta):
        model = ProfileTeacher
        fields = ProfileFullSerializer.Meta.fields + ('position',)


class ProfileStudentSerializer(ProfileFullSerializer):
    class Meta(ProfileFullSerializer.Meta):
        model = ProfileStudent
        fields = ProfileFullSerializer.Meta.fields + ('faculty',)
