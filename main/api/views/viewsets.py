import logging
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from ..models import Subject, TeacherSubject, SubjectStudent, AttendanceStudent, TakenSubject
from ..serializers import SubjectSerializer, TeacherSubjectSerializer, \
    SubjectStudentSerializer, TakenSubjectSerializer
from ..permissions import IsAllowedToViewAttendance, IsAllowedToCheckAttendance, \
    IsAllowedToViewTakenSubjectMarkStudents, IsAllowedToViewSubjectStudents, IsAllowedToCreateDiscipline
from ..serializers import AttendanceStudentSerializer, TeacherAttendanceStudentSerializer, \
    StudentTakenSubjectSerializer

logger = logging.getLogger(__name__)


class TeacherSubjectViewSet(mixins.RetrieveModelMixin,
                            mixins.DestroyModelMixin,
                            mixins.UpdateModelMixin,
                            viewsets.GenericViewSet):
    queryset = TeacherSubject.objects.all()
    serializer_class = TeacherSubjectSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class SubjectViewSet(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def perform_destroy(self, instance):
        logger.warning(f'Subject with {instance.id} id was deleted')
        logger.error(f'Subject with {instance.id} id was deleted')
        logger.critical(f'Subject with {instance.id} id was deleted')
        instance.delete()


class SubjectStudentViewSet(mixins.RetrieveModelMixin,
                            mixins.DestroyModelMixin,
                            mixins.UpdateModelMixin,
                            viewsets.GenericViewSet):
    queryset = SubjectStudent.objects.all()
    serializer_class = SubjectStudentSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class TeacherTakenSubjectStudentListViewSet(mixins.RetrieveModelMixin,
                                            mixins.UpdateModelMixin,
                                            mixins.DestroyModelMixin,
                                            viewsets.GenericViewSet):
    queryset = TakenSubject.objects.all()
    serializer_class = TakenSubjectSerializer
    permission_classes = (IsAuthenticated, IsAllowedToViewSubjectStudents)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    # def update(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)


class StudentTakenSubjectViewSet(mixins.RetrieveModelMixin,
                                 viewsets.GenericViewSet):
    queryset = TakenSubject.objects.all()
    serializer_class = StudentTakenSubjectSerializer
    permission_classes = (IsAuthenticated, IsAllowedToViewTakenSubjectMarkStudents)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class TeacherAttendanceStudentViewSet(mixins.RetrieveModelMixin,
                                      mixins.UpdateModelMixin,
                                      mixins.DestroyModelMixin,
                                      viewsets.GenericViewSet):
    queryset = AttendanceStudent.objects.all()
    serializer_class = TeacherAttendanceStudentSerializer
    permission_classes = (IsAuthenticated, IsAllowedToCheckAttendance)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class AttendanceStudentViewSet(mixins.RetrieveModelMixin,
                               viewsets.GenericViewSet):
    queryset = AttendanceStudent.objects.all()
    serializer_class = AttendanceStudentSerializer
    permission_classes = (IsAuthenticated, IsAllowedToViewAttendance)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
