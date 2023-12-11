from rest_framework import serializers

from apis.models import Employee


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ("id", "name", "address", "age", "salary")
