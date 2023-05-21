from django.db import models
from django.contrib.auth.models import User  

class Lecture(models.Model):
    lectName = models.CharField(max_length = 50)
    professor = models.CharField(max_length = 50)
    students = models.ManyToManyField(User)

    def __str__(self):
        return self.lectName

