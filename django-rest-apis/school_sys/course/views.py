from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course
from .serializers import CourseSerializer

# Create your views here.
class Courses(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializers = CourseSerializer(courses, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

class AddCourse(APIView):
    def post(self, request):
        serializers = CourseSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class GetUpdateDelete(APIView):
    def get_course_id(self, pk):
        try:
            return Course.objects.get(pk=pk)
        except:
            return Response(
                {
                    "errors": "Not found"
                }, status=status.HTTP_302_FOUND
            )

    def get(self, request, pk):
        course = self.get_course_id(pk)
        serializers = CourseSerializer(course)
        return Response(serializers.data)

    def put(self, request, pk):
        course = self.get_course_id(pk)
        serializers = CourseSerializer(course, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        course = self.get_course_id(pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

