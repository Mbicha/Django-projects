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

    def update(self, instance, data):
        instance.first_name = data.get('first_name', instance.first_name)
        instance.last_name = data.get('last_name', instance.last_name)
        instance.email = data.get('email', instance.email)
        instance.course = data.get('course', instance.course)
        instance.age = data.get('age', instance.age)

        instance.save()
        return instance