from django.contrib import admin

from student.models import student
from .models import *

# Register your models here.
admin.site.register(student)