from asyncio.windows_events import NULL
import profile
from django.db import models
from django.contrib.auth.models import User

from students.models import *
import uuid

from django.db.models.fields import CharField

class Profile(models.Model):
    MALE = 0
    FEMALE = 1
    GENDER_CHOICES = [(MALE, 'Male'), (FEMALE, 'Female')]
    user = models.OneToOneField(
        User, on_delete=models.CASCADE,blank=True, null=True
    )
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    gender = models.IntegerField(choices=GENDER_CHOICES)
    age = models.IntegerField(blank=True, null=True, default=0)
    course = models.ForeignKey(Course, on_delete=models.SET_DEFAULT, default="None")
    fee = models.ForeignKey(Fee, on_delete=models.SET_DEFAULT, default=0)

    def __str__(self):
        return self.email

class Location(models.Model):
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    profile = models.ForeignKey(Profile, on_delete=models.SET_DEFAULT, default="None")
    location_id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)

    def __str__(self):
        return "{}, {}, {}, {}, {}".format(
            self.email, self.country, self.city, self.street, self.address
        )

