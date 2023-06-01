from django.db import models
from django.contrib.auth.models import User 

class study(models.Model):
    name = models.CharField(max_length= 150)
    groupNum = models.IntegerField(default = 1) #그룹 인원수
    participant = models.ManyToManyField(User)
    relateLect = models.CharField(max_length = 150)


