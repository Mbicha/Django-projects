from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.registerUser, name='register-user'),
    path('students/', views.studentPortal, name='student-portal'),
    path('', views.tutorPortal, name="tutor-portal"),
    path('students/', views.home, name="home"),
]
