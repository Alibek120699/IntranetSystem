from rest_framework import status, viewsets, mixins, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .permissions import IsAllowedToCreateTeacherProfile, IsAllowedToCreateStudentProfile
from .serializers import MyUserSerializer, ProfileTeacherSerializer, ProfileStudentSerializer
from .models import MyUser, ProfileTeacher, ProfileStudent


class RegisterMyUserAPIView(APIView):
    http_method_names = ['post']
    permission_classes = (IsAdminUser,)

    def post(self, request):
        serializer = MyUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MyUserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MyUserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return MyUser.objects.all()

    @action(methods=['GET'], detail=False)
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)


class ProfileTeacherAPIView(mixins.CreateModelMixin,
                            mixins.ListModelMixin,
                            generics.GenericAPIView):
    http_method_names = ['get', 'post']
    queryset = ProfileTeacher.objects.all()
    serializer_class = ProfileTeacherSerializer
    permission_classes = (IsAuthenticated, IsAllowedToCreateTeacherProfile)

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


class ProfileStudentAPIView(mixins.CreateModelMixin,
                            mixins.ListModelMixin,
                            generics.GenericAPIView):
    http_method_names = ['get', 'post']
    queryset = ProfileStudent.objects.all()
    serializer_class = ProfileStudentSerializer
    permission_classes = [IsAuthenticated, IsAllowedToCreateStudentProfile]

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
