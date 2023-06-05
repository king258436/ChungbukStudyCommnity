from django.db import models
from django.contrib.auth.models import User  
from board.models import *

class Lecture(models.Model):
    lectName = models.CharField(max_length = 50)
    professor = models.CharField(max_length = 50)
    eval = models.ManyToManyField(evalLect)
    
    def __str__(self):
        return self.lectName
    
class LectList(models.Model):
    myLects = models.ManyToManyField(Lecture)
    username = models.CharField(max_length = 150)

    def __str__(self):
        return self.username
    
