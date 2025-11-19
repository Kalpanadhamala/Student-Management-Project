from django.db import models

class Student(models.Model):  # Changed to more appropriate name
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    grade = models.IntegerField()
    email = models.EmailField(max_length=100, unique=True)

    def __str__(self):
        return self.name


