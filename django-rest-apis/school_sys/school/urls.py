from django.urls import path
from .views import *

urlpatterns = [
    path('list/', SchoolList.as_view()),
    path('', CreateSchool.as_view()),
    path('<int:pk>/', GetUpdateDeleteSchool.as_view()),
]