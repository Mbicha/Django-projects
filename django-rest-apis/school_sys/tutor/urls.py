import django
from django import views


from django.urls import path
from .views import TutorsList, CreateTutor, GetUpdateDelete

urlpatterns = [
    path('list/', TutorsList.as_view()),
    path('', CreateTutor.as_view()),
    path('<int:pk>/', GetUpdateDelete.as_view()),
]
