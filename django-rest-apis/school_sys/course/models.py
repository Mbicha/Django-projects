from django.db import models
from matplotlib.pyplot import title

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=200)
    duration = models.IntegerField(default=0)
    number_of_units = models.IntegerField(default=0)
    cost = models.IntegerField(default=0)

    def __str__(self):
        return self.title