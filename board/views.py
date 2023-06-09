from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from django.core.paginator import Paginator
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
        postTag = request.POST.get('mySelect')
        postIt = Post()
        postIt.title = postTitle
        postIt.content = postContent
        postIt.author = postAuthor
        postIt.lectName = postLectName
        postIt.tag = postTag
        postIt.save()
        return redirect(f'/board/post/{lectName}') # 사용자를 게시판 페이지로 리디렉션
    return render(request, 'board/newpost.html', {'lectName' : lectName, 'lectList' :lectList})

def Posting(request,lectName,pk):
    post = Post.objects.get(pk=pk)
    try:
        lectList = LectList.objects.get(username = request.user.username).myLects.all()
    except:
        lectList = []
    try:
        likes = post.likes.get(username = request.user.username)
        likeit = 1
    except:
        likeit = 0
    if request.method == "POST":
        if 'delBtn' in request.POST:
            if post.author == request.user.username:  # 게시물 작성자만 게시물 삭제 권한 부여
                post.delete()
                return redirect(f'/board/post/{lectName}')
        elif 'likeBtn' in request.POST:
            try:
                likes = post.likes.get(username = request.user.username)
                likeit = 1
            except:
                me = like()
                me.username = request.user.username
                me.likeit = 1
                me.save()
                post.likes.add(me)
                post.save()
        elif 'dislikeBtn' in request.POST:
            likes = post.likes.get(username = request.user.username)
            likes.delete()
        elif 'commentBtn' in request.POST:
            mycomment = Comment()
            mycomment.content = request.POST.get('comments')
            mycomment.author = request.user.username
            mycomment.save()
            post.comments.add(mycomment)
        # 댓글 삭제 함수
        elif 'deleteCommentBtn' in request.POST:
            commentId = request.POST.get('commentId')
            try:
                comment = Comment.objects.get(id=commentId)
                if comment.author == request.user.username:
                    comment.delete()
            except Comment.DoesNotExist:
                pass
    context ={
        'lectName' : lectName,
        'pk' : pk, 
        'post' : post, 
        'likeit' : likeit,
        'comments' : post.comments.all(),
        'lectList' : lectList,
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
    
    paginator = Paginator(postList, 10)
    pageNum = request.GET.get('page')
    pageObj = paginator.get_page(pageNum)
    return render(request, "board/board.html", {'lectList' : lectList,'postList':pageObj, 'lectName' : lectName})

def lectInfo(request,lectName):
    if not request.user.is_authenticated:
        return redirect("main:home")
    lectList = LectList.objects.get(username = request.user.username)
    lectList = lectList.myLects.all()
    postList = Post.objects.filter(lectName = lectName, tag = "정보 글")
    
    paginator = Paginator(postList, 10)
    pageNum = request.GET.get('page')
    pageObj = paginator.get_page(pageNum)
    return render(request, "board/board.html", {'lectList' : lectList,'postList':pageObj, 'lectName' : lectName})

def lectQuest(request,lectName):
    if not request.user.is_authenticated:
        return redirect("main:home")
    lectList = LectList.objects.get(username = request.user.username)
    lectList = lectList.myLects.all()
    postList = Post.objects.filter(lectName = lectName, tag = "질문 글")
    
    paginator = Paginator(postList, 10)
    pageNum = request.GET.get('page')
    pageObj = paginator.get_page(pageNum)
    return render(request, "board/board.html", {'lectList' : lectList,'postList':pageObj, 'lectName' : lectName})

def evalMain(request):
    myLects = []
    if not request.user.is_authenticated:
        login = 0
    else:
        myLects = LectList.objects.get(username = request.user.username).myLects.all()
        login = 1
    evalList = list(evalLect.objects.all())
    evalC = len(evalList)
    if evalC > 4:
        evalList = evalList[evalC-4:evalC]
    lectCount = len(myLects)
    if request.method == 'POST':
        if 'searchBtn' in request.POST:
            lookingFor = []
            search = request.POST.get('search_subject')
            lectList = Lecture.objects.filter(lectName__icontains = search)
            for i in lectList:
                for j in i.eval.all():
                    lookingFor.append(j) #필요한 자료들을 넘겨받았슴동
            evalList = lookingFor
        elif 'evalBtn' in request.POST:
            lectC = int(request.POST.get('mySelect'))-1
            try:
                evalLect.objects.get(author = request.user.username, lectName = myLects[lectC].lectName)
            except:
                newEval = evalLect()
                newEval.content = request.POST.get('contents')
                newEval.rating = request.POST.get('ratingLect')
                newEval.lectName = myLects[lectC].lectName
                newEval.professor = myLects[lectC].professor
                newEval.author = request.user.username
                newEval.save()
                myLects[lectC].eval.add(newEval)
        elif 'delBtn' in request.POST:
            evalId = request.POST.get('evalId')
            try:
                evalObj = evalLect.objects.get(id=evalId)
                if evalObj.author == request.user.username:
                    evalObj.delete()
            except evalLect.DoesNotExist:
                pass

    context = {
        'myLects': myLects,
        'lectCount': lectCount,
        'login' : login,
        'evalList' : evalList,
    }
    return render(request, 'board/eval.html', context)

def myEval(request):
    if not request.user.is_authenticated:
        redirect('accounts:Login')
    evalList = evalLect.objects.filter(author = request.user.username)
    myLects = LectList.objects.get(username = request.user.username).myLects.all()
    lectCount = len(myLects)
    return render(request, 'board/myEval.html', {'evalList': evalList,'myLects': myLects,'lectCount': lectCount})

def evalBoard(request,lectName,professor):
    evalList = evalLect.objects.filter(lectName = lectName, professor = professor)
    myLects = LectList.objects.get(username = request.user.username).myLects.all()
    lectCount = len(myLects)
    context = {
        'myLects': myLects,
        'lectCount': lectCount,
        'lectName': lectName, 
        'professor':professor,
        'evalList':evalList,
    }
    return render(request, 'board/evalBoard.html', context)