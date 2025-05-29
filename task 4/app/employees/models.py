from django.db import models

# Create your models here.

class Employee(models.Model):
    emp_id = models.CharField(primary_key=True, max_length=20, verbose_name='Employee ID')
    emp_name = models.CharField(max_length=50, verbose_name='Employee Name')
    designation = models.CharField(max_length=50, verbose_name='Designation')

    def __str__(self):
        return self.emp_name
