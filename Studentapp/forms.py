from django import forms
from .models import Student  # Updated model name

class StudentForm(forms.ModelForm):  # Consistent naming
    class Meta:
        model = Student
        fields = ['name', 'age', 'email', 'grade']