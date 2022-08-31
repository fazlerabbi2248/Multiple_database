from django.db import models

# Create your models here.

class teacher(models.Model):
    GENDER = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('O', 'Other'),
    )
    T_ID = models.CharField(max_length=12, primary_key=True, default='16201519-001')
    T_name = models.CharField(max_length=50, default='')
    T_gender = models.CharField(max_length=1, choices=GENDER, default='M')
    T_class = models.CharField(max_length=50, default='')

