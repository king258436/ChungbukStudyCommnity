from django.urls import path
from . import views

urlpatterns = [
    path('MyPage/', views.MyPage, name='MyPage'),
]
# '/mypage/' URL로 접근할 때 'mypage' 함수 호출
