from django.db import models

class User(models.Model): #유저
    name = models.CharField(max_length = 30)
    age = models.IntegerField()
    user_id = models.CharField(max_length = 30)
    user_pw = models.CharField(max_length = 20)
    email = models.EmailField()
    
    def __str__(self): # __str__ : 객체를 print() 함수로 출력할 때나 문자열로 변환할 때 자동으로 호출되어 객체의 문자열 표현을 반환
        return self.user_id # 사용자의 user_id 반환

class Lecture(models.Model):
    professor = models.CharField(max_length = 10)
    lectName = models.CharField(max_length = 20)
    students = models.ManyToManyField(User)
    
    def __str__(self):
        return self.lectName # 강의명 반환
