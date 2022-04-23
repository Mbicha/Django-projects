from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),

    path('register-tutor/', views.createTutor, name='create-tutor'), 
    path('register-student/', views.registerUser, name='register-user'),    

    path('students-portal/', views.studentPortal, name='student-portal'),
    path('tutor-portal/', views.tutorPortal, name="tutor-portal"),   
]
