from django.urls import path
from . import views

urlpatterns = [
    path("list/", views.getStudents),
    path("<int:pk>", views.getStudentById),
    path('', views.createStudent),
]
