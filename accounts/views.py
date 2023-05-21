from django.contrib.auth import authenticate, login
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
    
def Forget(request):
    return render(request, 'accounts/ps_change.html')

def MyPage(request):
    userInfo = request.user
    myLects = LectList.objects.get(username = request.user.username)
    myLects = myLects.myLect.all()
    return render(request, 'accounts/MyPage.html', { 'MyLects' : myLects, 'userInfo' : userInfo})

def InfoChange(request):
    if request == 'POST':
        pass
    return render(request, 'accounts/MyPageInfoChange.html')
