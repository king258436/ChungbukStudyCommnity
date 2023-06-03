from django.contrib import admin
from django.urls import path, include
import os


urlpatterns = [
    path('admin/', admin.site.urls,name = 'toAdmin'),
    path('accounts/', include('accounts.urls')),
    path('', include('main.urls')),
    path('board/', include('board.urls')),
    path('study/', include('studygroup.urls')),
    
]
