from django.shortcuts import render
from accounts.models import *
from board.models import *

def index(request):
    lectList = []
    postinfo = []
    if request.user.is_authenticated:#로그인 됐음
        loginCheck = 1
        try:
            lectList = LectList.objects.get(username = request.user.username)
            lectList = lectList.myLects.all()
        except:
            lectList = LectList()
            lectList.username = request.user.username
            lectList.save()
    
        if len(lectList) > 0:
            haveLect = 1
        else:
            haveLect = 0
    else: #로그인 안돼있음 
        loginCheck = 0
        haveLect = 0
    hotPost = list(Post.objects.all())
    if len(hotPost) <=0:
        hotPost = []
        PostCheck = 0
    else:
        hotPost = hotPost[0:min(4,len(hotPost))]
        postinfo = []
        for i in hotPost:
            postinfo.append({'lectName' : i.lectName,'likeCount' : i.likeCount(), 'title' : i.title, 'pk' : i.pk })
        PostCheck =1
    context ={
        'lectList' : lectList,
        'loginCheck' : loginCheck,
        'haveLect' : haveLect,
        'postinfo' : postinfo,
        'PostCheck' : PostCheck,
    }
    return render(request, 'main/index.html', context)