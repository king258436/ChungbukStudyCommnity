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
        return redirect(f'/board/post/{lectName}') # 사용자를 게시판 페이지로 리디렉션
    return render(request, 'board/newpost.html', {'lectName' : lectName, 'lectList' :lectList})

def Posting(request,lectName,pk):
    post = Post.objects.get(pk=pk)
    try:
        likes = post.likes.get(username = request.user.username)
        if likes.likeIt:
            likeit = 1
        else:
            likeit = 0
    except:
        likeit = 0
    if request.method == "POST":
        if 'delBtn' in request.POST:
            post.delete()
            return redirect(f'/board/post/{lectName}')
        elif 'likeBtn' in request.POST:
            try:
                likes = post.likes.get(username = request.user.username)
                if likes.likeit:
                    likes.likeit = 0
                else:
                    likes.likeit = 1
            except:
                me = like()
                me.username, me.likeit = request.user.username, 1
                me.save()
                post.likes.add(me)
        elif 'commentBtn' in request.POST:
            mycomment = Comment()
            mycomment.content = request.POST.get('comments')
            mycomment.author = request.user.username
            mycomment.save()
            post.comments.add(mycomment)
    context ={
        'lectName' : lectName,
        'pk' : pk, 
        'post' : post, 
        'likeit' : likeit,
        'comments' : post.comments.all()
    }
    return render(request, "board/posting.html", context)

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

def evalMain(request):
    myLects = []
    if not request.user.is_authenticated:
        login = 0
    else:
        myLects = LectList.objects.get(username = request.user.username).myLects.all()
        login = 1
    eval = evalLect.objects.all()
    lectCount = len(myLects)
    context = {
        'myLects': myLects,
        'lectCount': lectCount,
        'login' : login,
        'evals' : eval,
    }
    return render(request, 'board/eval.html', context)

def evalBoard(request,lectName):
    return render(request, 'board/evalPost.html', {'lectName', lectName})