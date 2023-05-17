from django.db import models
from django.contrib.auth.models import User  

class Student(models.Model):
    studentName = models.CharField(max_length = 150)

    def __str__(self):
        return self.studentName

class Lecture(models.Model):
    lectName = models.CharField(max_length = 50)
    professor = models.CharField(max_length = 50)
    students = models.ManyToManyField(Student)



