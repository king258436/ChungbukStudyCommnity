from django.urls import path, include
from main.views import *


urlpatterns = [
    path('', index, name='index'),
]