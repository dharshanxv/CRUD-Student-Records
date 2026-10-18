from django.db import models

class Student(models.Model):
    roll_number = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    course = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.roll_number})"