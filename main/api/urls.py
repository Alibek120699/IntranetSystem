from django.urls import path
from rest_framework.routers import DefaultRouter


from .views import SubjectStudentListCreateAPIView, SubjectStudentViewSet, \
    TeacherSubjectListCreateAPIView, TeacherSubjectViewSet, \
    SubjectCreateListAPIView, SubjectViewSet, TeacherTakenSubjectStudentListViewSet, TeacherTakenSubjectCreateApiView, \
    TeacherAttendanceStudentViewSet, StudentTakenSubjectViewSet, AttendanceStudentViewSet, StudentTakenSubjectApiView, \
    AttendanceStudentAPIView, TeacherAttendanceStudentCreateAPIView, NewsListAPIView

from .views import subject_view, subject_detail_view

urlpatterns = [
    path('subjects/', SubjectCreateListAPIView.as_view()),
    path('fbv_subjects/', subject_view),
    path('fbv_subjects/<int:pk>/', subject_detail_view),
    path('teacher_subjects/', TeacherSubjectListCreateAPIView.as_view()),
    path('subject_students/', SubjectStudentListCreateAPIView.as_view()),
    path('taken_subject_teacher/', TeacherTakenSubjectCreateApiView.as_view()),
    path('taken_subject_student/', StudentTakenSubjectApiView.as_view()),
    path('teacher_add_attendance/', TeacherAttendanceStudentCreateAPIView.as_view()),
    path('check_student_attendance/', AttendanceStudentAPIView.as_view()),
    path('news/', NewsListAPIView.as_view()),
]

router = DefaultRouter()
router.register('subjects', SubjectViewSet, basename='subjects')
router.register('teacher_subjects', TeacherSubjectViewSet, basename='teacher_subjects')
router.register('subject_students', SubjectStudentViewSet, basename='subject_students')
router.register('taken_subject_teacher', TeacherTakenSubjectStudentListViewSet, basename='taken_subject_teacher')
router.register('taken_subject_student', StudentTakenSubjectViewSet, basename='taken_subject_student')
router.register('check_student_attendance', AttendanceStudentViewSet, basename='check_student_attendance')
router.register('teacher_add_attendance', TeacherAttendanceStudentViewSet, basename='teacher_add_attendance')
urlpatterns += router.urls

