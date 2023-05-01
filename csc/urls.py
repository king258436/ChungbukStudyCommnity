from django.contrib import admin
from django.urls import path
from accounts import views as AcView

urlpatterns = [
    path('admin/', admin.site.urls,name = 'toadmin'),
    path('accounts/Register/', AcView.Register, name = 'Register'),
]
