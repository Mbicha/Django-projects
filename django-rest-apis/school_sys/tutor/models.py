from django.db import models
from django.forms import CharField

# Create your models here.
class Tutor(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    unit_tutoring = models.CharField(max_length=200)
    level_education = models.CharField(max_length=200)

    def __str__(self):
        return self.full_name