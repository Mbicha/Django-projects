from ast import Mod
from pickle import TRUE
from random import choices
from django.db import models
import uuid

from djmoney.models.fields import MoneyField

from utils.utils import jsontotuple

# Create your models here.
class Course(models.Model):
    course_path = "utils/data/course.json"
    COURSE_CHOICES = jsontotuple(course_path)
    title = models.CharField(max_length=200, choices=COURSE_CHOICES)
    cost = MoneyField(
        decimal_places=2,
        default=0,
        max_digits=12,
    )
    duration = models.IntegerField(default=4)
    course_id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)

    def __str__(self):
        return self.title

class Fee(models.Model):
    total_fee = MoneyField(
        decimal_places=2,
        default=0,
        max_digits=12,
    )

    fee_paid = MoneyField(
        decimal_places=2,
        default=0,
        max_digits=12,
    )

    email = models.CharField(max_length=200)
    fee_id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)

    def __str__(self):
        return self.student_reg_num

class Exam(models.Model):
    MIDTERM = 0
    FINAL = 1
    EXAM_CHOICES = [
        (MIDTERM, 'Mid-Term Exam'), (FINAL, 'Final Exam'),
    ]
    exam_date = models.Field()
    exam_type = models.IntegerField(choices=EXAM_CHOICES)
    course_title = models.ForeignKey(Course, on_delete=models.DO_NOTHING)

