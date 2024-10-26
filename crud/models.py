from django.db import models

class Office(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Employees(models.Model):
    employee_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    date_of_joining = models.DateField()
    department = models.CharField(max_length=100)
    office = models.ForeignKey(Office, on_delete=models.CASCADE, related_name='employees')

    def __str__(self):
        return self.name
