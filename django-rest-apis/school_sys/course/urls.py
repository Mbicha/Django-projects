from django.urls import path
from .views import *

urlpatterns = [
    path('list/', Courses.as_view()),
    path('', AddCourse.as_view()),
    path('<int:pk>/', GetUpdateDelete.as_view()),
]
