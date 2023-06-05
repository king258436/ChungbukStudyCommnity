from django.db import models
from django.contrib.auth.models import User 

class study(models.Model):
    name = models.CharField(max_length = 150)
    tag = models.CharField(max_length = 10, default= '모집 중')
    purpose = models.CharField(max_length = 200,default='')
    author = models.CharField(max_length = 150, default='NoNamed')
    groupNum = models.IntegerField(default = 1) #그룹 인원수
    title = models.CharField(max_length = 150, default='Empty title')
    summary = models.TextField(default='')
    contents = models.TextField(default='')

    def __str__ (self):
        return self.title


