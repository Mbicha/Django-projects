from attr import fields
from .models import *
from rest_framework import serializers

class StudentSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.CharField()
    course = serializers.CharField()
    age = serializers.CharField()
    
    def create(self, data):
        return Student.objects.create(**data)
