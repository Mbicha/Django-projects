from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="index"),
    path("signup/", views.createUser, name="signup"),
    path("create-profile/", views.createProfile, name='create_profile'),
]
