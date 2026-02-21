from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # These are the fields we want to send as JSON
        fields = ['id', 'studentname', 'rollnumber', 'password'] 