from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import *

app_name = 'studyGroup'

urlpatterns = [
    path('', Main, name = 'Main'),
    path('study/posting', NewPosting, name = 'NewStudy'),
    path('study/<str:studyName>', Posting, name = 'Posting')
]