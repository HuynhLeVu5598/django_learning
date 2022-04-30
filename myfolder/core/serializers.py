from rest_framework import serializers
from .models import Course

class GetAllCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id',)

class CourseSerializer(serializers.Serializer):
    title1 = serializers.CharField(max_length=12)
    content1 = serializers.CharField(max_length=12)
    price1 = serializers.IntegerField() 