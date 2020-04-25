from rest_framework import status, mixins, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.permissions import IsAllowedToCreateTeacherSubject,\
    IsAllowedToCreateSubjectStudent, IsAllowedToCreateDiscipline
from api.models import Subject, TeacherSubject, SubjectStudent
from api.serializers import SubjectSerializer, TeacherSubjectSerializer,\
    SubjectStudentSerializer


class TeacherSubjectListCreateAPIView(mixins.CreateModelMixin,
                                      mixins.ListModelMixin,
                                      generics.GenericAPIView):
    http_method_names = ['get', 'post']
    queryset = TeacherSubject.objects.all()
    serializer_class = TeacherSubjectSerializer
    permission_classes = (IsAuthenticated, IsAllowedToCreateTeacherSubject)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = TeacherSubjectSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)





class SubjectStudentListCreateAPIView(mixins.ListModelMixin,
                                      mixins.CreateModelMixin,
                                      generics.GenericAPIView):
    http_method_names = ['get', 'post']
    queryset = SubjectStudent.objects.all()
    serializer_class = SubjectStudentSerializer
    permission_classes = (IsAuthenticated, IsAllowedToCreateSubjectStudent)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class SubjectCreateListAPIView(mixins.CreateModelMixin,
                               mixins.ListModelMixin,
                               generics.GenericAPIView):
    http_method_names = ['post', 'get']
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = (IsAllowedToCreateDiscipline, )

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
