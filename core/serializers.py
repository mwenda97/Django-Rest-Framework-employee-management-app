from rest_framework import serializers
from .models import *

class DeparmentSerilizers(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('DepartmentId','DepartmentName')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('EmployeeId','EmployeeName','Department','DateOfJoining','ProfileName')