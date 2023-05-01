from django.db import models

class User(models.Model): #유저
    name = models.CharField(max_length = 30)
    age = models.IntegerField()
    user_id = models.CharField(max_length = 30)
    user_pw = models.CharField(max_length = 20)
    email = models.CharField(max_length = 50)

    def __str__(self):
        return self.user_id

