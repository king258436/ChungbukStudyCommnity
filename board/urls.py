from .views import *
from django.urls import path

app_name = 'board'

urlpatterns = [
    path('', index, name = 'home'),
    path('post/<str:lectName>', lectBoard, name = 'board'),
    path('post/<str:lectName>/newPost/', NewPost, name='NewPost'),
    path('post/<str:lectName>/see/<int:pk>/', Posting, name ='Posting'),
    path('test/', test, name='test'),
    path('test2/', test2, name='test2'),
    path('test2/newstudy/', NewStudy, name='newstudy'),
    path('test2/StdPost', StdPost, name='StdPost'),
]