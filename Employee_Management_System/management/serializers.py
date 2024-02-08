from rest_framework import serializers
from .models import Department, Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['name', 'employee_id', 'title']

class DepartmentSerializer(serializers.ModelSerializer):
    employees = EmployeeSerializer(many=True, read_only=True)

    class Meta:
        model = Department
        fields = ['id', 'name', 'employees']
