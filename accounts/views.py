from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect
from .models import *
from .forms import UserForm

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password) 
            # 사용자 인증
            login(request, user)  # 로그인
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'accounts/SignUp.html', {'form': form})

#마이 페이지에서 사용할 함수 

def Home(request):
    return render(request, 'accounts/home.html')
    
def Forget(request):
    return render(request, 'accounts/ps_change.html')


