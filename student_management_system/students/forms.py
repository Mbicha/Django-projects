from pyexpat import model
from attr import fields
from django.forms import ModelForm
from django import forms
from .models import Student, Instructor

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields =  [
            'first_name', 'last_name', 'student_email', 'student_tel',
            'gender', 'location', 'date_of_birth'
        ]

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

class TutorForm(ModelForm):
    class Meta:
        model = Instructor

        fields = [
            'full_name', 'instructor_email', 'salary'
        ]

    def __init__(self, *args, **kwargs):
        super(TutorForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})