from email.policy import default
from django.db import models
from django.contrib.auth.models import User

import uuid
# Create your models here.
class StudentProfile(models.Model):
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_CHOICE = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
    
    user = models.OneToOneField(
        User, on_delete=models.CASCADE,blank=True, null=True
    )
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    student_email = models.CharField(max_length=200)
    password = models.CharField(max_length=16, default=1234)
    profile_image = models.ImageField(
        blank=True, null=True, upload_to="student_profile/", default="student_profile/profile.svg"
    )
    student_tel = models.CharField(max_length=13)
    gender = models.IntegerField(choices=GENDER_CHOICE)
    location = models.CharField(max_length=200, null=True, blank=True)
    date_of_birth = models.CharField(max_length=10)
    date_joined = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)

    def __str__(self):
        return self.first_name

class InstructorProfile(models.Model):
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_CHOICE = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
    
    user = models.OneToOneField(
        User, on_delete=models.CASCADE,blank=True, null=True
    )
    full_name = models.CharField(max_length=200, null=True, blank=True)
    instructor_email = models.CharField(max_length=200, null=True, blank=True)
    password = models.CharField(max_length=16, default=1234)
    profile_image = models.ImageField(
        blank=True, null=True, upload_to="tutor_profile/", default="tutor_profile/profile.svg"
    )
    gender = models.IntegerField(choices=GENDER_CHOICE)
    salary = models.DecimalField(max_digits=16, decimal_places=2)
    start_date = models.DateTimeField(auto_now_add=True)    
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)

    def __str__(self):
        return self.full_name
