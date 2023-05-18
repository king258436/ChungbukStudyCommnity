from django.urls import path, include
from django.contrib.auth import views as auth_views
from accounts.views import *

app_name = 'accounts'

urlpatterns = [
    path('Login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name = 'Login') ,
    path('Logout/', auth_views.LogoutView.as_view(), name = 'Logout'),
    path('Forget/', Forget, name = 'PsChange'),
    path('SignUp/', SignUp, name = 'SignUp'),
    path('MyPage/', MyPage, name = 'MyPage')
]
