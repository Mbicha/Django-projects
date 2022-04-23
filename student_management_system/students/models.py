from venv import create
from click import Choice
from django.db import models
import uuid

# Create your models here.
class Student(models.Model):
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_CHOICE = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
    
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    student_email = models.CharField(max_length=200)
    student_tel = models.CharField(max_length=13)
    gender = models.IntegerField(choices=GENDER_CHOICE)
    location = models.CharField(max_length=200, null=True, blank=True)
    date_of_birth = models.CharField(max_length=10)
    date_joined = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)

    def __str__(self):
        return self.first_name

class Attendance(models.Model):
    offering_id = models.CharField(max_length=200, null=True, blank=True)
    student_email = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=16, decimal_places=2)
    date_filled = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)

    def __str__(self):
        return self.offering_id
        

class Instructor(models.Model):
    full_name = models.CharField(max_length=200, null=True, blank=True)
    instructor_email = models.CharField(max_length=200, null=True, blank=True)
    salary = models.DecimalField(max_digits=16, decimal_places=2)
    start_date = models.DateTimeField(auto_now_add=True)    
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)

    def __str__(self):
        return self.full_name

class Course(models.Model):
    course_code = models.CharField(max_length=20, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    course_code = models.CharField(max_length=20, null=True, blank=True)
    duration = models.CharField(max_length=20, null=True, blank=True)
    amount_paid = models.DecimalField(max_digits=16, decimal_places=2)
    start_date = models.DateTimeField(auto_now_add=True)    
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)

    def __str__(self):
        return self.title

class Offering(models.Model):
    offering_id = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    instructor_email = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    course_code = models.ForeignKey(Course, on_delete=models.CASCADE)
    num_of_students = models.IntegerField(default=0, null=True, blank=True)
    start_date = models.DateTimeField(auto_now_add=True)    
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
