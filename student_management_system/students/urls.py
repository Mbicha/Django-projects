from django.urls import path
from . import views

urlpatters = [
    path('', views.registerUser, name='register-user'),
]
