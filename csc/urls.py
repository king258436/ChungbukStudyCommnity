from django.contrib import admin
from django.urls import path
from accounts import views as AcView
import os


urlpatterns = [
    path('admin/', admin.site.urls,name = 'toAdmin'),
    path('accounts/Register/', AcView.Register, name = 'Register'),
    path('accounts/Login/', AcView.Login, name = 'Login'),
    path('', AcView.Home,name = 'home')
]
