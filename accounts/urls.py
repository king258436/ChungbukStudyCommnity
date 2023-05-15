from django.urls import path, include
from accounts.views import *

urlpatterns = [
    path('Login/', Login, name = 'Login') ,
    path('SignUp/', Register, name = 'Register'),
    path('Forget/', Forget, name = 'PsChange'),
    path('MyPage/', MyPage, name='MyPage'),
]
