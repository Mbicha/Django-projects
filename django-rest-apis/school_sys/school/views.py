from django.shortcuts import render
from requests import delete
from rest_framework.views import APIView
from .serializers import SchoolSerializer
from .models import School
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class SchoolList(APIView):
    def get(self, request):
        schools = School.objects.all()
        serilizers = SchoolSerializer(schools, many=True)
        return Response(serilizers.data, status=status.HTTP_200_OK)

class CreateSchool(APIView):
    def post(self, request):
        serializers = SchoolSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)

        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class GetUpdateDeleteSchool(APIView):
    def get_school_id(self, pk):
        try:
            return School.objects.get(pk=pk)
        except:
            return Response(
            {
                "errors": "No such a school"
            }, status=status.HTTP_404_NOT_FOUND
        )

    def get(self, request, pk):
        school = self.get_school_id(pk)
        serializer = SchoolSerializer(school)
        return Response(serializer.data)

    def put(self, request, pk):
        school = self.get_school_id(pk)
        serializer = SchoolSerializer(school, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        school = self.get_school_id(pk)
        school.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

