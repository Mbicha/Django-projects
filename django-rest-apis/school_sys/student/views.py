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
        return Response(seriralizer._errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def getStudentById(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except:
        return Response(
            {
                'errors': "Student doesn't exist"
            }, status=status.HTTP_404_NOT_FOUND
        )

    if request.method == 'GET':
        serializer = StudentSerializers(student)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = StudentSerializers(student, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
