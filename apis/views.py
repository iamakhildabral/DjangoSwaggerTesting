from django.shortcuts import render
from rest_framework import viewsets

from apis.models import Employee
from apis.serializer import EmployeeSerializer

# Create your views here.


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
