from django.contrib.auth import authenticate, login, models
from django.shortcuts import render,redirect
from .models import *
from .forms import UserForm

def SignUp(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'accounts/SignUp.html', {'form': form})

#마이 페이지에서 사용할 함수 

def Home(request):
    return render(request, 'accounts/home.html')

def MyPage(request):
    userInfo = request.user
    myLects = LectList.objects.get(username = request.user.username)
    myLects = myLects.myLect.all()
    return render(request, 'accounts/mypage/MyPage.html', { 'MyLects' : myLects, 'userInfo' : userInfo})

def InfoChange(request):
    if request.method == 'POST':
        pass
    return render(request, 'accounts/mypage/MyPageInfoChange.html')

def PsChange(request):
    if request.method == 'POST':
        pass
    return render(request, 'accounts/PsChange.html')

def Forget(request):
    warn = "동무, 그런 아이디는 존재하지 않습네다!"
    error = 0
    if request.method == "POST":
        userName = request.POST.get('username')
        try:#해당 이름을 가진 유저가 존재합디다.
            valid = User.objects.get(Username = userName)
            return render(request, 'accounts/PsChange.html')
        except: # 아니오 동무 그렇지 않습네다.
            error = 1
    return render(request, 'accounts/Forget.html', {'warning' : warn, 'error' : error})

def ManageSub(request):
    if request.method == "POST":
        pass
    return render(request, 'accounts/mypage/ManageSub.html')
