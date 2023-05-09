from django.db import models

class User(models.Model): #유저
    name = models.CharField(max_length = 30)
    age = models.IntegerField()
    user_id = models.CharField(max_length = 30)
    user_pw = models.CharField(max_length = 20)
    email = models.EmailField()

class Lecture(models.Model):
    professor = models.CharField(max_length = 10)
    lectName = models.CharField(max_length = 20)
    students = models.ManyToManyField(User)
