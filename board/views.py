from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from .models import *
from accounts.models import *

def NewPost(request,lectName): #게시판 렌더링 함수
    lectList = LectList.objects.get(username = request.user.username)
    lectList = lectList.myLects.all()
    if request.method == 'POST':   #POST 요청인지 확인, POST 요청이면 새로운 게시물 생성
        postTitle = request.POST.get('postname')
        postContent = request.POST.get('contents')
        postAuthor = request.user.username
        postLectName = lectName
        postIt = Post()
        postIt.title = postTitle
        postIt.content = postContent
        postIt.author = postAuthor
        postIt.lectName = postLectName
        postIt.save()
        return redirect('board:home') # 사용자를 게시판 페이지로 리디렉션
    return render(request, 'board/newpost.html', {'lectName' : lectName, 'lectList' :lectList})

def Posting(request,lectName,pk):
    post = Post.objects.get(pk=pk)
    return render(request, "board/posting.html", {'lectName' : lectName, 'pk' : pk, 'post' : post})

# 로그인한 사용자에게만 게시판 표시하는 함수
def index(request):
    if not request.user.is_authenticated:
        return redirect("main:home")
    lectList = LectList.objects.get(username = request.user.username)
    lectList = lectList.myLects.all()
    return render(request, "board/main.html", {"lectList": lectList})

def lectBoard(request,lectName):
    if not request.user.is_authenticated:
        return redirect("main:home")
    lectList = LectList.objects.get(username = request.user.username)
    lectList = lectList.myLects.all()
    postList = Post.objects.filter(lectName = lectName)
    return render(request, "board/board.html", {'lectList' : lectList,'postList':postList, 'lectName' : lectName})
