from rest_framework import serializers
from .models import *

class CourseSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=120)
    description = serializers.CharField(max_length=120)
    code = serializers.IntegerField()

class ClassSerializer(serializers.Serializer):
    course = serializers.IntegerField()
    name = serializers.CharField(max_length=120)
    description = serializers.CharField(max_length=120)

class ClassPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ('name', 'description',)
        
class SectionSerializer(serializers.Serializer):
    _class = serializers.IntegerField()
    name = serializers.CharField()
    
class ExamTermGetSerializer(serializers.Serializer):
    name = serializers.CharField()
