from django.urls import path, include
from accounts.views import *

urlpatterns = [
    path('Login/', Login, name = 'Login') ,
    path('SignUp/', Register, name = 'Register'),
    path('Forget/', Forget, name = 'psChange'),
    path('MyPage/', MyPage, name = 'myPage'),

]