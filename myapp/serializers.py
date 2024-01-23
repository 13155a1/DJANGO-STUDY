from rest_framework import serializers
from .models import Student

class BaseStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        # fields = ('studentID', 'name', 'major')