from django.shortcuts import render
from .forms import StudentForm


# Create your views here.
def registerUser(request):
    form = StudentForm()
    context = {'form':form}
    return render(request, 'students/signup.html', context)

def home(request):
    return render(request, 'students/home.html')

def studentPortal(request):
    return render(request, 'students/student-portal.html')

def tutorPortal(request):
    return render(request, 'students/tutor-portal.html')