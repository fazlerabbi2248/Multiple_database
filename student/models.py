from django.db import models

# Create your models here.

class student(models.Model):
    GENDER = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('O', 'Other'),
    )
    std_ID = models.CharField(max_length=12, primary_key=True, default='16201519-001')
    std_name = models.CharField(max_length=50, default='')
    std_gender = models.CharField(max_length=1, choices=GENDER, default='M')
    std_class = models.CharField(max_length=50, default='')
