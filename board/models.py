from django.db import models

class Comment(models.Model):
    content = models.TextField()
    pubDate = models.DateTimeField()
    author = models.CharField(max_length=15)

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    pubDate = models.DateTimeField()
    author = models.CharField(max_length=15)
    lectName = models.CharField(max_length=20)
    comments = models.ManyToManyField(Comment)
