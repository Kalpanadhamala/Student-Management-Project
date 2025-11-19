from django.contrib import admin
from .models import Student  # Updated to match new model name

admin.site.register(Student)