from django.contrib.auth import authenticate, login, models
from django.shortcuts import render,redirect
from .models import *
from .forms import UserForm

def SignUp(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/index.html')
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
    return render(request, 'accounts/mypage/MyPageInfoChange.html')

def PsChange(request,userName):
    user = User.objects.get(username = userName)
    error = 0
    if request.method == 'POST':
        pwd = request.POST.get('pwd')
        pwdConfirm = request.POST.get('pwdConfirm')
        print(pwd)
        print(pwdConfirm)
        if(pwd!=pwdConfirm):
            error=1
            return render(request, 'accounts/PsChange.html', {'username' : userName, 'error' : error})
        else:
            user.set_password(pwd)
            user.save()
            return render(request, 'accounts/login.html')
    return render(request, 'accounts/PsChange.html', {'username' : userName, 'error' : error})

def Forget(request):
    warn = "동무, 그런 아이디는 존재하지 않습네다!"
    error = 0
    if request.method == "POST":
        userName = request.POST.get('username')
        print(userName)
        url = '/accounts/PsChange/'+userName
        print(url)
        return redirect(url)
    return render(request, 'accounts/Forget.html', {'warning' : warn, 'error' : error})

def ManageSub(request):
    if request.method == "POST":
        pass
    return render(request, 'accounts/mypage/ManageSub.html')
