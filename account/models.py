from django.db import models

class id(models.Model):
    id_ = models.CharField(max_length=16)

class pw(models.Model):
    pw_ = models.Charfield(max_length=20)

class user(models.Model):
    name = models.CharField(max_length=30)
    gender = models.IntegerField(defalut = 0) #0 - male 1 - female
    PostCount = models.IntegerField(defalut = 0)

