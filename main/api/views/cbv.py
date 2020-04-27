import logging

from rest_framework import status, mixins, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..permissions import IsAllowedToCreateTeacherSubject, \
    IsAllowedToCreateSubjectStudent, IsAllowedToCreateDiscipline, IsAllowedToViewTakenSubjectMarkStudents, \
    IsAllowedToViewSubjectStudents, IsAllowedToCheckAttendance, IsAllowedToViewAttendance
from ..models import Subject, TeacherSubject, SubjectStudent, TakenSubject, AttendanceStudent, News
from ..serializers import SubjectSerializer, TeacherSubjectSerializer, \
    SubjectStudentSerializer, StudentTakenSubjectSerializer, TakenSubjectSerializer, TeacherAttendanceStudentSerializer, \
    AttendanceStudentSerializer, NewsSerializer

logger = logging.getLogger(__name__)


class TeacherSubjectListCreateAPIView(mixins.CreateModelMixin,
                                      mixins.ListModelMixin,
                                      generics.GenericAPIView):
    http_method_names = ['get', 'post']
    # queryset = TeacherSubject.objects.all()
    queryset = TeacherSubject.objects.select_related('subject', 'teacher')
    serializer_class = TeacherSubjectSerializer
    # permission_classes = (IsAuthenticated, IsAllowedToCreateTeacherSubject)

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
    serializer_class = SubjectStudentSerializer
    # permission_classes = (IsAuthenticated, IsAllowedToCreateSubjectStudent)

    def get_queryset(self):
        return SubjectStudent.objects.select_related('student', 'subject')

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
    # permission_classes = (IsAllowedToCreateDiscipline,)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        logger.debug(f'Subject with {serializer.instance.id} id was created')
        logger.info(f'Subject with {serializer.instance.id} id was created')
        logger.warning(f'Subject with {serializer.instance.id} id was created')
        logger.error(f'Subject with {serializer.instance.id} id was created')
        logger.critical(f'Subject with {serializer.instance.id} id was created')
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class TeacherTakenSubjectCreateApiView(mixins.ListModelMixin,
                                       mixins.CreateModelMixin,
                                       generics.GenericAPIView):
    http_method_names = ['get', 'post']
    queryset = TakenSubject.objects.all()
    serializer_class = TakenSubjectSerializer
    permission_classes = (IsAuthenticated, IsAllowedToViewSubjectStudents)

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


class StudentTakenSubjectApiView(mixins.ListModelMixin,
                                 generics.GenericAPIView):
    http_method_names = ['get']
    queryset = TakenSubject.objects.all()
    serializer_class = StudentTakenSubjectSerializer
    permission_classes = (IsAuthenticated, IsAllowedToViewTakenSubjectMarkStudents)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class TeacherAttendanceStudentCreateAPIView(mixins.ListModelMixin,
                                            mixins.CreateModelMixin,
                                            generics.GenericAPIView):
    http_method_names = ['get', 'post']
    queryset = AttendanceStudent.objects.all()
    serializer_class = TeacherAttendanceStudentSerializer
    permission_classes = (IsAuthenticated, IsAllowedToCheckAttendance)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        logger.debug(f'Attendance to Student with {serializer.instance.id} id was added')
        logger.info(f'Attendance to Student with {serializer.instance.id} id was added')
        logger.warning(f'Attendance to Student with {serializer.instance.id} id was added')
        logger.error(f'Attendance to Student with {serializer.instance.id} id was added')
        logger.critical(f'Attendance to Student with {serializer.instance.id} id was added')
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class AttendanceStudentAPIView(mixins.ListModelMixin,
                               generics.GenericAPIView):
    http_method_names = ['get']
    queryset = AttendanceStudent.objects.all()
    serializer_class = AttendanceStudentSerializer
    permission_classes = (IsAuthenticated, IsAllowedToViewAttendance)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class NewsListAPIView(mixins.ListModelMixin,
                      generics.GenericAPIView):
    http_method_names = ['get']
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
