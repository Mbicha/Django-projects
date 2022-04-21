from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.registerUser, name='register-user'),
    path('', views.studentPortal, name='student-portal'),
    path('students/', views.home, name="home"),
]
