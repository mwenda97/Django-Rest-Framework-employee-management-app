from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
# Create your views here.

class DepartmentView(viewsets.ModelViewSet):
    serializer_class = DeparmentSerilizers
    queryset = Department.objects.all()

class EmployeeView(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
