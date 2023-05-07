from .views import bulletinBoard
from django.urls import path

urlpatterns = [
    path('bulletinBoard/', bulletinBoard, name = ' Board')
]
