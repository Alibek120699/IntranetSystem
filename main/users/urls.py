from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter

from .views import RegisterMyUserAPIView, MyUserViewSet


urlpatterns = [
    path('login/', obtain_jwt_token),
    path('register/', RegisterMyUserAPIView.as_view()),
]

router = DefaultRouter()
router.register('users', MyUserViewSet, basename='users')

urlpatterns += router.urls
