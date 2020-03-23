from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import SubjectStudentListCreateAPIView, SubjectStudentViewSet,\
    TeacherSubjectListCreateAPIView, TeacherSubjectViewSet,\
    SubjectCreateListAPIView, SubjectViewSet


urlpatterns = [
    path('subjects/', SubjectCreateListAPIView.as_view()),
    path('teacher_subjects/', TeacherSubjectListCreateAPIView.as_view()),
    path('subject_students/', SubjectStudentListCreateAPIView.as_view()),
]

router = DefaultRouter()
router.register('subjects', SubjectViewSet, basename='subjects')
router.register('teacher_subjects', TeacherSubjectViewSet, basename='teacher_subjects')
router.register('subject_students', SubjectStudentViewSet, basename='subject_students')
urlpatterns += router.urls

