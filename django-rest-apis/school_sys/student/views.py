from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializers

# Create your views here.
@api_view(['GET'])
def getStudents(request):
    students = Student.objects.all()
    serializer = StudentSerializers(students, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createStudent(request):
    seriralizer = StudentSerializers(data=request.data)
    if seriralizer.is_valid():
        seriralizer.save()
        return Response(seriralizer.data)
    else:
        return Response(seriralizer._errors)

@api_view(['GET'])
def getStudentById(request, pk):
    if request.method == 'GET':
        student = Student.objects.get(pk=pk)
        serializer = StudentSerializers(student)
        return Response(serializer.data)
