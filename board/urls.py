from .views import *
from django.urls import path

app_name = 'board'

urlpatterns = [
    path('', Vision, name='Vision'),
    # URL:80/blog/숫자로 접속하면 게시글-세부페이지(posting)
    path('<int:pk>/', Posting, name='Posting'),
    path('new_post/', NewPost, name='NewPost'),
    path('<int:pk>/remove/', RemovePost, name = "RemovePost"),   
]