# your_app/models.py
from django.db import models

class Infirmier(models.Model):
    name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=50, unique=True)
    department = models.CharField(max_length=100)
    # Add other fields as needed

    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    medical_record_id = models.CharField(max_length=50, unique=True)
    # Add other fields as needed

    def __str__(self):
        return self.name