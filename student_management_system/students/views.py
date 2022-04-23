from django.shortcuts import redirect, render
from .models import Student, Instructor
from .forms import StudentForm, TutorForm


# Create your views here.
def registerUser(request):
    page = 'student'
    form = StudentForm()

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('student-portal')

    context = {'form':form, 'page':page}
    return render(request, 'students/signup.html', context)

def createTutor(request):
    page = 'tutor'

    form = TutorForm()

    if request.method == 'POST':
        form = TutorForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('tutor-portal')

    context = {'form': form}

    return render(request, 'students/signup.html', context)
"""
def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            student = Student.objects.get(email=student)
            tutor = Instructor.objects.get(email=tutor)
"""

def home(request):
    return render(request, 'students/home.html')

def studentPortal(request):
    return render(request, 'students/student-portal.html')

def tutorPortal(request):
    return render(request, 'students/tutor-portal.html')