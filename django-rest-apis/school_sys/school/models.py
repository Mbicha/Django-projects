from xml.parsers.expat import model
from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    vision = models.CharField(max_length=2000, blank=True, null=True)
    mission = models.CharField(max_length=2000, blank=True, null=True)
    values = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name
