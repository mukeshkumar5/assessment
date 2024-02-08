from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100)
    employee_id = models.IntegerField()
    title = models.CharField(max_length=100)
    department = models.ForeignKey(Department, related_name='employees', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.employee_id}"

